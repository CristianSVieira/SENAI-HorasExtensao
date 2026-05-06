from fastapi import APIRouter
from database.connection import get_db_connection
from app.schemas.for_users import LoginSchema
from app.services.auth_service import realizar_login_service

router = APIRouter(prefix="/autenticacao", tags=["Acesso"])


@router.post("/entrar")
def entrar(dados: LoginSchema):
    db = get_db_connection()
    try:
        return realizar_login_service(db, dados.cpf, dados.senha)
    finally:
        db.close()