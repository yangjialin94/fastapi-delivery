import aiohttp

class HttpClient:
    session: aiohttp.ClientSession = None

    def start(self):
        self.session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=100, limit_per_host=0))

    async def stop(self):
        await self.session.close()
        self.session = None

    def __call__(self) -> aiohttp.ClientSession:
        assert self.session is not None
        return self.session

http_client = HttpClient()
