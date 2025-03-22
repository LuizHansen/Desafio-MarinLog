from dotenv import load_dotenv, find_dotenv
import os
import pymssql 

dotenv_file = find_dotenv(usecwd=True)
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
# Carrega o arquivo .env
load_dotenv(dotenv_file)

# Configurações da APP
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
RELOAD = os.getenv("RELOAD")

# Configurações banco de dados
DB_SGDB = os.getenv("DB_SGDB")
DB_NAME = os.getenv("DB_NAME")
# Caso seja diferente de sqlite
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

SQLALCHEMY_DATABASE_URL = f"mssql+pymssql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"