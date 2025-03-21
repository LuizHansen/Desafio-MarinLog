from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class CnabTyping(BaseModel):
    id_transacao: Optional[int] = None
    tipo_transacao: int
    data_transacao: date
    valor_transacao: float
    cpf_transacao: int
    cartao_transacao: str
    hora_transacao: time
    dono_da_loja: str
    nome_da_loja: str