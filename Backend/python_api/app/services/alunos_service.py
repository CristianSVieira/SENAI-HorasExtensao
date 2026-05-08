from ..database.connection import get_db_connection
from fastapi import HTTPException

def get_progresso_aluno(id_aluno: int):

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    try:
        # Busca aluno + carga horária do curso
        cursor.execute("""
            SELECT
                u.id        AS id_aluno,
                u.nome,
                c.nome      AS nome_curso,
                c.carga_horas_extensao
            FROM usuario u
            JOIN curso c ON c.id = u.id_curso
            WHERE u.id = %s
        """, (id_aluno,))
        aluno = cursor.fetchone()

        if not aluno:
            raise HTTPException(status_code=404, detail="Aluno não encontrado.")

        # Soma as horas validadas
        cursor.execute("""
            SELECT COALESCE(SUM(horas_homologadas), 0) AS horas_validadas
            FROM solicitacao_horas_aluno
            WHERE id_aluno = %s
              AND status = 'Validado'
        """, (id_aluno,))
        resultado = cursor.fetchone()

        horas_validadas = float(resultado["horas_validadas"])
        carga_total = float(aluno["carga_horas_extensao"] or 0)

        progresso = min((horas_validadas / carga_total) * 100, 100.0) if carga_total > 0 else 0.0

        return {
            "id_aluno": aluno["id_aluno"],
            "nome": aluno["nome"],
            "curso": aluno["nome_curso"],
            "horas_validadas": horas_validadas,
            "carga_horas_extensao": carga_total,
            "progresso_percentual": round(progresso, 2)
        }

    finally:
        cursor.close()
        db.close()