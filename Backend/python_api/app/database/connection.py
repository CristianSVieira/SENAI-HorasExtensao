from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from core.config import DATABASE_URL

from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()

def get_db(): 
    session = Session()
    try:
        yield session
    finally:
        session.close()
       


# PARA TESTE

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass   