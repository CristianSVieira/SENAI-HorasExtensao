import os
from dotenv import load_dotenv

#Esta linha lê o arquivo .env e carrega as variáveis no sistema
load_dotenv()
#Endereço do Banco de Dados
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://senaihe:senha_do_db@127.0.0.1:3306/senai_horas_extensao")
#Chaves de Segurança para o Login 
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
#Tempo de expiração do login
TOKEN_EXPIRATION = int(os.getenv("TOKEN_EXPIRATION"))