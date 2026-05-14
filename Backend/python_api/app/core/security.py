from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import os

# Configurações de ambiente
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def verificar_senha(senha_plana, senha_hash):
    """Compara a senha enviada com o hash salvo"""
    return pwd_context.verify(senha_plana, senha_hash)

def gerar_hash_senha(senha: str):
    """Gera hash seguro para armazenamento"""
    return pwd_context.hash(senha)

def criar_token_acesso(dados: dict):
    """Cria token JWT com tempo de expiração do .env"""
    to_encode = dados.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str = Depends(oauth2_scheme)):
    """
    Decodifica o token. 
    Tratamento de erros e validação de banco ficam na camada de rotas.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None