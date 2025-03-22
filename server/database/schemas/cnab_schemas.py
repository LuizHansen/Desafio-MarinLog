from sqlalchemy import String, Column, Integer, DateTime, BigInteger, DECIMAL, Time
from db import base

class CnabSchema(base):
    __tablename__ = 'tb_transacoes'

    id_transacao = Column(Integer, primary_key=True, autoincrement=True, index=True)
    tipo_transacao = Column(Integer, nullable=False)
    data_transacao = Column(DateTime, nullable=False)
    valor_transacao = Column(DECIMAL(10,2), nullable=False)
    cpf_transacao = Column(BigInteger, nullable=False)
    cartao_transacao = Column(String(12), nullable=False)
    hora_transacao = Column(Time, nullable=False)
    dono_da_loja = Column(String(14), nullable=False)
    nome_da_loja = Column(String(19), nullable=False)

