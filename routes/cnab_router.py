from cnab_typings import CnabModel
from fastapi import APIRouter, status, UploadFile, File
from controllers.cnab_controller import controller_get_cnab, controller_post_cnab

cnab_router = APIRouter()

@cnab_router.get(status_code=status.HTTP_200_OK)
async def get_cnab():
    return await controller_get_cnab

@cnab_router.post(status_code=status.HTTP_201_CREATED)
async def post_cnab(file: UploadFile = File(...)):
    conteudo_arquivo = await file.read()
    return await controller_post_cnab(conteudo_arquivo)