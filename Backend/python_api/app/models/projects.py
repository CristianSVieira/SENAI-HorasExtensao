from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.connection import Base 

class Projeto(Base):
    __tablename__ = "projeto" 

    id_projeto: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(String(255), nullable=True) 
    horas_previstas: Mapped[int] = mapped_column(nullable=False)
    id_docente: Mapped[int] = mapped_column(ForeignKey("docente.id_docente"), nullable=False)
    id_curso: Mapped[int] = mapped_column(ForeignKey("curso.id_curso"), nullable=False)

# Tabelas de apoio - PARA TESTE
class Curso(Base):
    __tablename__ = "curso"
    id_curso: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False) 

class Docente(Base):
    __tablename__ = "docente"
    id_docente: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False) # Adicionado String(100)