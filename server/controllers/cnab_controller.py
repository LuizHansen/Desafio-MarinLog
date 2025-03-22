from services.cnab_service import CnabService 

class CnabController:

    async def controller_get_cnab(self):
        try:
            return await CnabService().service_get_cnab()
        except Exception as e:
            return {"mensagem": e}

    async def controller_post_cnab(self, conteudo_arquivo):
        try:
            return await CnabService().service_post_cnab(conteudo_arquivo)
        except Exception as e:
            return {"mensagem": e}
