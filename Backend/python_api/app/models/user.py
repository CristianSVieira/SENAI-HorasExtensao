#modelo de banco pros usuarios
class User:
    def __init__(self, id_usuario, nome, cpf, email, senha_hash, tipo_perfil):
        self.id_usuario = id_usuario
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha_hash = senha_hash
        self.tipo_perfil = tipo_perfil # ALUNO ou DOCENTE