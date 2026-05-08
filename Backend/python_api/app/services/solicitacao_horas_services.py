from datetime import datetime
import uuid
from database.connection import get_db_connection

def criar_solicitacao_service(data):
    if not data.comprovante:
        raise ValueError("O comprovante precisa ser enviado.")

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        query = """
        INSERT INTO solicitacao_horas_aluno
        (id, id_projeto, status, id_aluno, data_postagem, comprovante, observacao_aluno)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            str(uuid.uuid4()),
            data.id_projeto,
            "Pendente",
            data.id_aluno,
            datetime.now(),
            data.comprovante,
            data.observacao_aluno
        )

        cursor.execute(query, values)
        conn.commit()

        return {"message": "Solicitação criada."}

    finally:
        cursor.close()
        conn.close()

def listar_solicitacoes(id_aluno: str):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        query = """
        SELECT *
        FROM solicitacao_horas_aluno
        WHERE id_aluno = %s
        ORDER BY data_postagem DESC
        """

        cursor.execute(query, (id_aluno,))
        solicitacoes = cursor.fetchall()

        return solicitacoes

    finally:
        cursor.close()
        conn.close()

def aluno_existe(id_aluno: str):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        query = """
        SELECT id
        FROM usuario
        WHERE id = %s
        AND role = 'Aluno'
        """

        cursor.execute(query, (id_aluno,))
        aluno = cursor.fetchone()

        return aluno

    finally:
        cursor.close()
        conn.close()