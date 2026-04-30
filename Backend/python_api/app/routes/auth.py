from fastapi import APIRouter, HTTPException
from database.connection import get_db_connection
from app.services.auth_services import realizar_login_service
from app.schemas.for_users import LoginSchema

# Prefixo atualizado para /autenticacao 
router = APIRouter(prefix="/autenticacao", tags=["Acesso"])

@router.post("/entrar") # Nome do endpoint corrigido 
def entrar(dados: LoginSchema):
    db = get_db_connection()
    try:
        return realizar_login_service(db, dados.cpf, dados.senha)
    finally:
        db.close()

# Novo endpoint para retornar dados do usuário logado 
@router.get("/usuario/perfil")
def obter_perfil():
    # Retorna nome, email e role conforme o Guia [cite: 18]
    return {"msg": "Retorna os dados do usuário logado (nome, email, role)"}