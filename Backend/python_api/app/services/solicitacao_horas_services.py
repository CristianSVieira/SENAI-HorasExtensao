from fastapi import HTTPException
from datetime import datetime
import uuid
from database.connection import get_db_connection

def criar_solicitacao_service(data):
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

    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao criar a solicitação")

    finally:
        cursor.close()
        conn.close()
