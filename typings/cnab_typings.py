from pydantic import BaseModel
from typing import Optional

class CnabTyping(BaseModel):
    id_transacao: Optional[int] = None
    tipo_transacao: int
    data_transacao: int
    valor_transacao: int
    cpf_transacao: int
    cartao_transacao: int
    hora_transacao: int
    dono_da_loja: str
    nome_da_loja: str