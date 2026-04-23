from datetime import datetime
from database.connection import get_db_connection

# TODO: trocar de DB_FAKE para o banco de dados real (model da dupla 4)
# Cristian - Sem DB_Fake, busca direta do DB, mas com esta correção citada pendente
def get_solicitacao_horas_por_status(status:str):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM solicitacao_horas_aluno where status=%s", (status,))
        return cursor.fetchall()
    finally:
        cursor.close()
        db.close()


# TODO: trocar de DB_FAKE para o banco de dados real (model da dupla 4)
# TODO: trocar campos solicitados para schema de request 
def update_status_solicitacao_horas(id_solicitacao_horas:str, status_solicitacao_horas:str, horas_homologadas:int, observacao_aluno:str, comentario_docente:str):
    db = get_db_connection()
    cursor = db.cursor(dictionary=False)
    data_hora_agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        cursor.execute("UPDATE solicitacao_horas_aluno set status=%s, horas_homologadas=%s, observacao_aluno=%s, comentario_docente=%s, data_processamento=%s where id=%s", (status_solicitacao_horas, horas_homologadas, observacao_aluno, comentario_docente, data_hora_agora, id_solicitacao_horas))
        return { "mensagem": "Solicitação de Horas atualizada com sucesso" }
    finally:
        cursor.close()
        db.close()
        
    return None
