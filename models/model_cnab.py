from database.schemas.cnab_schemas import CnabSchema
from typings.cnab_typings import CnabTyping
import db

session = db.SessionLocal()

class CnabModel:

    async def model_get_cnab():
        return session.query(CnabSchema).all()

    async def model_post_cnab(self, dados_arquivo: CnabSchema):
        novo_cnab = CnabSchema(**dados_arquivo.model_dump())
        session.add(novo_cnab)
        return {"Mensagem": f"Cnab cadastrado com sucesso: {novo_cnab.id_transacao}"}