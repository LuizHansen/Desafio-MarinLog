from database.schemas.cnab_schemas import CnabSchema
from typings.cnab_typings import CnabTyping
import db as db

session = db.SessionLocal()

class CnabModel:

    async def model_get_cnab(self): 
        return session.query(CnabSchema).all()

    async def model_post_cnab(self, dados_arquivo: list[CnabTyping]):
        try:
            for cnab_obj in dados_arquivo:
                novo_cnab = CnabSchema(**cnab_obj.model_dump())
                session.add(novo_cnab)

            session.commit()
            return {"mensagem": f"{len(dados_arquivo)} registros CNAB cadastrados com sucesso!"}

        except Exception as e:
            session.rollback()
            return {"error": f"Erro ao inserir no banco de dados: {str(e)}"}