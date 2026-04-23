from fastapi import APIRouter, HTTPException
from services import solicitacao_horas_services as service

router = APIRouter(prefix="/solicitacao_horas", tags=["horas"])

# TODO: trocar response_model para schema de response
@router.get("/{status}", response_model=object)
async def get_solicitacoes_por_status(status:str):
    return service.get_solicitacao_horas_por_status(status)


# TODO: trocar response_model para schema de response
# TODO: trocar campos solicitados para schema de request 
@router.put("/{id}", response_model=object)
async def update_solicitacao_horas(id:str, status_solicitacao_horas:str, horas_homologadas:int, comentario_aluno:str, comentario_docente:str):
    resultado = service.update_status_solicitacao_horas(id, status_solicitacao_horas, horas_homologadas, comentario_aluno, comentario_docente)

    if not resultado:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada no sistema.")
        
    return resultado
