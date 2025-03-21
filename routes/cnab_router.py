from fastapi import APIRouter, status, UploadFile, File
from controllers.cnab_controller import CnabController

cnab_router = APIRouter(prefix="/cnab")

@cnab_router.get("/consultar_cnab", status_code=status.HTTP_200_OK)
async def get_cnab():
    return await CnabController().controller_get_cnab()

@cnab_router.post("/enviar_cnab", status_code=status.HTTP_201_CREATED)
async def post_cnab(file: UploadFile = File(...)):
    conteudo_arquivo = await file.read()
    return await CnabController().controller_post_cnab(conteudo_arquivo)