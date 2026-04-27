from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.for_projects import ProjetoCreate, ProjetoRead, ProjetoUpdate, ProjetoDelete
from app.services import project_services as service
from app.services import solicitacao_horas_services as sh_service

router = APIRouter(prefix="/projeto", tags=["Projeto"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def cadastrar(project_data: ProjetoCreate):
    try:
        # TODO: Validação do id do docente em autorização
        return service.cadastrar_projeto(project_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

@router.get("/{id}", response_model=ProjetoRead)
def listar_por_id(id: str = None):
    try:
        return service.listar_projeto_por_id(id=id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

@router.get("/{id_curso}", response_model=List[ProjetoRead])
def listar(id_curso: str = None):
    return service.listar_projetos(id_curso=id_curso)

@router.delete("/")
def excluir(dados: ProjetoDelete):
    # TODO: Validação da autorização para excluir
    
    # Verifica se o projeto pode ser encontrado
    try:
        projeto_por_id = service.listar_projeto_por_id(dados)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Projeto não encontrado")
    
    # Se sim, verifica-se se ele pode ser encontrado nas solicitações de horas
    if sh_service.listar_qualquer_solicitacao_para_projeto(dados) is not None:
        raise HTTPException(status_code=404, detail="Existe uma solitação de horas pendente para este projeto e não pode ser excluído até que se resolva.")
    else:
        try:
            return service.excluir_projeto(dados)
        except Exception as e:
            raise HTTPException(status_code=404, detail="O projeto não pôde ser excluído")

@router.put("/")
def editar(project_data: ProjetoUpdate):
    try:
        # TODO: Validação da autorização para editar
        return service.editar_projeto(project_data)
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)
