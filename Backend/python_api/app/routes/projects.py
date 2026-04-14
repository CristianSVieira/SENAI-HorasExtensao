from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.for_projects import ProjetoCreate, ProjetoRead
from app.services import project_services as service

router = APIRouter(prefix="/projetos", tags=["projetos"])

@router.post("", response_model=ProjetoRead) 
async def create_project(project_data: ProjetoCreate, db: Session = Depends(get_db)):
    
    # Aguardando a Dupla de Auth para trocar o 'current_user' .
    
    id_professor_logado = 1 
    return service.create_project(db, project_data, id_professor_logado)

@router.get("", response_model=list[ProjetoRead])
async def list_projects(id_curso: int = None, db: Session = Depends(get_db)):
    return service.get_projects(db, id_curso=id_curso)

@router.delete("/{id}") 
async def delete_project(id: int, db: Session = Depends(get_db)):
    return service.delete_project(db, id)
