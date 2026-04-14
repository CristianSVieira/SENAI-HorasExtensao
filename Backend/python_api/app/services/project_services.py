from sqlalchemy.orm import Session
from sqlalchemy import select, func
from app.models.projects import Projeto
from app.schemas.for_projects import ProjetoCreate
from fastapi import HTTPException, status

def create_project(db: Session, projeto_data: ProjetoCreate, professor_id: int):
    novo_projeto = Projeto(
        titulo=projeto_data.titulo,             
        descricao=projeto_data.descricao,      
        horas_previstas=projeto_data.horas_previstas,
        id_curso=projeto_data.id_curso,         
        id_docente=professor_id               
    )
    db.add(novo_projeto)
    db.commit()
    db.refresh(novo_projeto)
    return novo_projeto

def get_projects(db: Session, id_curso: int = None):
    query = db.query(Projeto)
    if id_curso:
        query = query.filter(Projeto.id_curso == id_curso) 
    return query.all()

def delete_project(db: Session, projeto_id: int):
    """
    Implementa a REGRA DE OURO: Bloqueia exclusão se houver vínculos.
    """
    projeto = db.query(Projeto).filter(Projeto.id_projeto == projeto_id).first()
    
    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado.")

    # --- LÓGICA DE INTEGRIDADE REFERENCIAL  ---
    # VERIFICAR SE EXISTEM SOLICITAÇÕES LIGADAS AO PROJETO
    # comentado até que a Dupla 4 crie o model de solicitações:
    
    # tem_vinculo = db.query(Solicitacao).filter(Solicitacao.id_projeto == projeto_id).first()
    # if tem_vinculo:
    #    raise HTTPException(
    #        status_code=status.HTTP_400_BAD_REQUEST,
    #        detail="Exclusão proibida: Existem solicitações vinculadas a este projeto."
    #    )

    db.delete(projeto)
    db.commit()
    return {"message": "Projeto excluído com sucesso."}