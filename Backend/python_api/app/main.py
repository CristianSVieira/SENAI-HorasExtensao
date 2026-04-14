from fastapi import FastAPI
from app.database.connection import engine, Base

#  Importe os modelos para o SQLAlchemy "enxergá-los"
from app.models.projects import Projeto, Curso, Docente 

#  Importe os módulos das rotas individualmente
from app.routes import auth, admin, students, professors, projects

app = FastAPI()

# Criar tabelas no startup
@app.on_event("startup")
def startup_event():
    print("Iniciando criação de tabelas...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas verificadas/criadas com sucesso!")


app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(students.router)
app.include_router(professors.router)
app.include_router(projects.router)

@app.get("/")
def read_root():
    return {"status": "Sistema de Horas de Extensão Ativo"}