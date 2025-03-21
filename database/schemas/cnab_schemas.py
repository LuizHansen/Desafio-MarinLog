from sqlalchemy import String, Column, Integer
from db import Base

class CnabSchema(Base):
    __tablename__ = 'tb_transacoes'

    id_transacao = Column(Integer, primary_key = True, autoincrement = True, index = True)
    tipo_transacao = Column(Integer(1), nullable=False)
    data_transacao = Column(Integer(8), nullable=False)
    valor_transacao = Column(Integer(10), nullable=False)
    cpf_transacao = Column(Integer(11), nullable=False)
    cartao_transacao = Column(String(12), nullable=False)
    hora_transacao = Column(Integer(6), nullable=False)
    dono_da_loja = Column(String(14), nullable=False)
    nome_da_loja = Column(String(19), nullable=False)

