import aiohttp
from aiohttp import TCPConnector

class HTTPClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self._session = None

    async def create_session(self):
        # Отключение SSL проверки
        connector = TCPConnector(ssl=False)
        self._session = await aiohttp.ClientSession(
            base_url=self.base_url,
            headers={
                'X-CMC_PRO_API_KEY': self.api_key,
            },
            connector=connector
        ).__aenter__()

    async def close(self):
        if self._session:
            await self._session.__aexit__(None, None, None)


class CMCHTTPClient(HTTPClient):
    async def get_listings(self):
        if not self._session:
            await self.create_session()  # Убедись, что сессия создана
        async with self._session.get("/v1/cryptocurrency/listings/latest") as response:
            result = await response.json()
            return result["data"]

    async def get_currency(self, currency_id: int):
        if not self._session:
            await self.create_session()  # Убедись, что сессия создана
        async with self._session.get(
            "/v2/cryptocurrency/quotes/latest",
            params={"id": currency_id}
        ) as response:
            result = await response.json()
            return result["data"], [str(currency_id)]