from app.database.connection import get_db_connection
from fastapi import HTTPException, status
from typing import List, Optional, Dict, Any
from app.schemas.for_projects import ProjetoCreate, ProjetoUpdate, ProjetoDelete

def listar_projetos(id_curso: Optional[str] = None) -> List[Dict[str, Any]]:
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        if id_curso is not None:
            cursor.execute("SELECT * FROM projeto WHERE id_curso = %s", (id_curso,))
        result = cursor.fetchall()
        return result
    finally:
        cursor.close()
        db.close()

def listar_projeto_por_id(id: str):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        if id is not None:
            cursor.execute("SELECT * FROM projeto WHERE id = %s", (id,))
        return cursor.fetchone()
    except Exception as e:
        raise Exception("O projeto não foi encontrado")
    finally:
        cursor.close()
        db.close()

def cadastrar_projeto(dados: ProjetoCreate) -> Dict[str, str]:
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute("""
            INSERT INTO projeto (id_docente, id_curso, titulo, descricao, horas_previstas)
            VALUES (%s, %s, %s, %s, %s)
        """, (dados.id_docente, dados.id_curso, dados.titulo, dados.descricao, dados.horas_previstas))
        db.commit()
        return {"message": "Projeto cadastrado com sucesso"}
    except Exception as e:
        db.rollback()
        raise Exception(f"Erro ao cadastrar: {str(e)}")
    finally:
        cursor.close()
        db.close()

def excluir_projeto(dados: ProjetoDelete) -> Dict[str, str]:
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("DELETE FROM projeto WHERE id = %s", (dados.id,))
        db.commit()
        return {"message": "Projeto excluído com sucesso."}
    except Exception as e:
        raise Exception(f"Erro ao excluir: {str(e)}")
    finally:
        cursor.close()
        db.close()

def editar_projeto(dados: ProjetoUpdate) -> Optional[Dict[str, str]]:
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM projeto WHERE id = %s", (dados.id,))
        projeto_atual = cursor.fetchone()
        
        if not projeto_atual:
            return None

        novo_titulo = dados.titulo or projeto_atual["titulo"]
        nova_descricao = dados.descricao or projeto_atual["descricao"]
        novas_horas = dados.horas_previstas if dados.horas_previstas is not None else projeto_atual["horas_previstas"]
        novo_curso = dados.id_curso or projeto_atual["id_curso"]

        cursor.execute("""
            UPDATE projeto 
            SET titulo=%s, descricao=%s, horas_previstas=%s, id_curso=%s
            WHERE id = %s
        """, (novo_titulo, nova_descricao, novas_horas, novo_curso, dados.id))
        
        db.commit()
        return {"message": "Projeto atualizado com sucesso"}
    except Exception as e:
        db.rollback()
        raise Exception(f"Erro ao atualizar: {str(e)}")
    finally:
        cursor.close()
        db.close()
