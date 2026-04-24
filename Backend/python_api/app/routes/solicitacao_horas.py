from fastapi import APIRouter
from schemas.solicitacao_horas import SolicitacaoRequest
from services.solicitacao_horas_services import criar_solicitacao_service

router = APIRouter(prefix="/solicitacoes", tags=["Solicitações"])

@router.post("")
def criar_solicitacao(data: SolicitacaoRequest):
    return criar_solicitacao_service(data)
