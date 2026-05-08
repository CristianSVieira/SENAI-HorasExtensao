from fastapi import APIRouter, HTTPException
from schemas.solicitacao_horas import SolicitacaoRequest
from services.solicitacao_horas_services import criar_solicitacao_service, listar_solicitacoes, aluno_existe

router = APIRouter(prefix="/solicitacoes", tags=["Solicitações"])

@router.post("")
def criar_solicitacao(data: SolicitacaoRequest):
    try:
        return criar_solicitacao_service(data)
    
    except ValueError as erro:
        raise HTTPException(status_code= 400, detail= erro)

@router.get("/{id_aluno}")
def listar_solicitacoes_do_aluno(id_aluno: str):
    if not aluno_existe(id_aluno):
            raise HTTPException(status_code= 404, detail= f"Aluno com o Id {id_aluno} não encontrado.")
        
    return listar_solicitacoes(id_aluno)