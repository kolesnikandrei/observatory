
# Async context managers should only be there if you want to await inside the enter and exit blocks.
async def get_conn():
    pass
    # await some awaitable obj


class Connection:
    def _init_(self, host, port):  # initializing the object
        self.host = host
        self.port = port

    async def _aenter_(self):  # setting up a connection
        self.conn = await get_conn(self.host, self.port)
        return conn

    async def _aexit_(self, exc_type, exc, tb):  # closing the connection
        await self.conn.close()


async with Connection('localhost', 500) as conn:
    pass
    # addfunctionality here