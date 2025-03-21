import pandas as pd

from models.model_cnab import CnabModel


class CnabService:

    async def service_get_cnab():
        return

    async def service_post_cnab(self, conteudo_arquivo):
        conteudo_arquivo = conteudo_arquivo.decode("utf-8")
        try:
            cnab_columns = [
                ("tipo", 0, 1),
                ("data", 1, 9),
                ("valor", 10, 19),
                ("cpf", 19, 30),
                ("cartao", 30, 42),
                ("hora", 43, 48),
                ("dono_da_loja", 48, 62),
                ("nome_da_loja", 62, 81)
            ]

            linhas = conteudo_arquivo.splitlines()

            dados_arquivo = []
            for linha in linhas:
                registro = {col[0]: linha[col[1]:col[2]].strip() for col in cnab_columns}

                registro["tipo"] = int(registro["tipo"])
                registro["valor"] = int(registro["valor"]) / 100
                registro["data"] = pd.to_datetime(registro["data"], format="%Y%m%d").date()
                registro["hora"] = pd.to_datetime(registro["hora"], format="%H%M%S").time()

                dados_arquivo.append(registro)

            df = pd.DataFrame(dados_arquivo)
            return await CnabModel().model_post_cnab(dados_arquivo)

        except Exception as e:
            return {"error": f"Erro ao processar CNAB: {str(e)}"}
            
        return 
