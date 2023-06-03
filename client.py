import aiohttp
import aiohttp.client_ws
import asyncio

async def recv(ws: aiohttp.client_ws.ClientWebSocketResponse):
    print("Waiting for message")
    await ws.receive()

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('http://localhost:8765/test') as ws:
            await ws.send_str("Hello World!")

            # close the connection with code 1000
            await ws.close(code=1000)


asyncio.run(main())
