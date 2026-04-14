from pydantic import BaseModel
from typing import Optional

class ProjetoBase(BaseModel):
    titulo: str
    descricao: str 
    horas_previstas: int 
    id_curso: int

class ProjetoCreate(ProjetoBase):
    pass 

class ProjetoRead(ProjetoBase):
    id_projeto: int
    id_docente: int

    class Config:
        from_attributes = True