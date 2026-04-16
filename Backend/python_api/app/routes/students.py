from fastapi import APIRouter
from database import get_session
from services.students_service import get_progresso_aluno

router = APIRouter(prefix="/students", tags=["students"])

@router.post("/request")
async def post_request():
    return {"request": "request"}

@router.get("/request")
async def get_all_requests(id:int):
    return {"request": id}

@router.get("/request/{id}")
async def get_request_by_idt(id:int):
    return {"request": id}

@router.get("/{id_aluno}/progress")
def progresso_aluno(id_aluno: int, db: Session = Depends(get_db)):
    return get_progresso_aluno(id_aluno, db)
