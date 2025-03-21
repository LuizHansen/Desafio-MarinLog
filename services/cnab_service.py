import pandas as pd
from typings.cnab_typings import CnabTyping
from database.schemas.cnab_schemas import CnabSchema
from models.model_cnab import CnabModel


class CnabService:

    async def service_get_cnab():
        return

    async def service_post_cnab(self, conteudo_arquivo):
        conteudo_arquivo = conteudo_arquivo.decode("utf-8")
        try:
            cnab_columns = [
                ("tipo_transacao", 0, 1),
                ("data_transacao", 1, 9),
                ("valor_transacao", 10, 19),
                ("cpf_transacao", 19, 30),
                ("cartao_transacao", 30, 42),
                ("hora_transacao", 43, 48),
                ("dono_da_loja", 48, 62),
                ("nome_da_loja", 62, 81)
            ]

            linhas = conteudo_arquivo.splitlines()

            dados_arquivo = []
            for linha in linhas:
                registro = {col[0]: linha[col[1]:col[2]].strip() for col in cnab_columns}

                registro["tipo_transacao"] = int(registro["tipo_transacao"])
                registro["valor_transacao"] = int(registro["valor_transacao"]) / 100
                registro["data_transacao"] = pd.to_datetime(registro["data_transacao"], format="%Y%m%d").date()
                registro["hora_transacao"] = pd.to_datetime(registro["hora_transacao"], format="%H%M%S").time()

                cnab_obj = CnabTyping(**registro)
                dados_arquivo.append(cnab_obj)
                
            
            return await CnabModel().model_post_cnab(dados_arquivo)

        except Exception as e:
            return {"error": f"Erro ao processar CNAB: {str(e)}"}
            
         
