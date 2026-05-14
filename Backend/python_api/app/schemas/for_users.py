from pydantic import BaseModel

class LoginSchema(BaseModel):
    cpf: str # Recebe o CPF para login
    senha: str # Recebe a senha para login

class UserPerfilSchema(BaseModel):
    # Dados para as telas de Perfil do Aluno e Docente
    nome: str
    email: str
    cpf: str
    tipo_perfil: str