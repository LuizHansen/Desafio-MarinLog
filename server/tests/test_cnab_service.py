import pytest
import pandas as pd
from services.cnab_service import CnabService

@pytest.mark.asyncio
async def test_processamento_cnab():
    """Testa se o CNAB é processado corretamente"""
    
    cnab_mock = """3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO"""
    
    service = CnabService()
    result = await service.service_post_cnab(cnab_mock.encode("utf-8"))

    assert "error" not in result, f"Erro inesperado: {result}"
