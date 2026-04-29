from fastapi import APIRouter
from schemas.solicitacao_horas import SolicitacaoRequest
from services.solicitacao_horas_services import criar_solicitacao_service, listar_solicitacoes

router = APIRouter(prefix="/solicitacoes", tags=["Solicitações"])

@router.post("")
def criar_solicitacao(data: SolicitacaoRequest):
    return criar_solicitacao_service(data)

@router.get("aluno/{id_aluno}")
def listar_solicitacoes_do_aluno(id_aluno: str):
    return listar_solicitacoes(id_aluno)
