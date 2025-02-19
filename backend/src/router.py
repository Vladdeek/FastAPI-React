from fastapi import APIRouter
from src.init import cmc_client


router = APIRouter(
    prefix="/cryptocurrencies"
)

@router.get("")
async def get_cryptocurrencies():
    return await cmc_client.get_listings()  # Добавьте await для асинхронного вызова


@router.get("{currency_id}")
async def get_cryptocurrency(currency_id: int):
    return await cmc_client.get_currency(currency_id)  # Добавьте await для асинхронного вызова
