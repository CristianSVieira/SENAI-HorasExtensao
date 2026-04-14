from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db

router = APIRouter()

@router.get("/aluno/{id_aluno}/progresso")
def get_progresso_aluno(id_aluno: int, db: Session = Depends(get_db)):

    # Busca aluno + carga horária do curso
    query_aluno = text("""
        SELECT
            u.id        AS id_aluno,
            u.nome,
            c.nome      AS nome_curso,
            c.carga_horas_extensao
        FROM usuario u
        JOIN curso c ON c.id = u.id_curso
        WHERE u.id = :id_aluno
    """)
    aluno = db.execute(query_aluno, {"id_aluno": id_aluno}).mappings().first()

    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")

    # Soma as horas validadas
    query_horas = text("""
        SELECT COALESCE(SUM(horas_homologadas), 0) AS horas_validadas
        FROM solicitacao_horas_aluno
        WHERE id_aluno = :id_aluno
          AND status = 'Validado'
    """)
    resultado = db.execute(query_horas, {"id_aluno": id_aluno}).mappings().first()

    # Retorna os dados brutos para o parceiro completar
    return {
        "id_aluno": aluno["id_aluno"],
        "nome": aluno["nome"],
        "curso": aluno["nome_curso"],
        "horas_validadas": float(resultado["horas_validadas"]),
        "carga_horas_extensao": float(aluno["carga_horas_extensao"] or 0),
        "progresso_percentual": min(
        float((resultado["horas_validadas"] / aluno["carga_horas_extensao"]) * 100 if aluno["carga_horas_extensao"] else 0),
        100.0
      )
    }