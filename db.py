from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import SQLALCHEMY_DATABASE_URL
from sqlalchemy.ext.declarative import declarative_base

# Criando o engine de conexão
engine = create_engine(SQLALCHEMY_DATABASE_URL)

base = declarative_base()

# Criando a sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()        
def cria_tabelas():
    base.metadata.create_all(engine, checkfirst=True)