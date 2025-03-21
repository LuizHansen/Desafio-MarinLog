from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import SQLALCHEMY_DATABASE_URL

# Criando o engine de conexão
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Criando a sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()