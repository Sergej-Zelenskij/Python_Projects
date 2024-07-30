import asyncio
import websockets
CONNECTIONS = set()

async def Register(websocket):
    CONNECTIONS.add(websocket)
    try:
        message = await websocket.recv()
        print(message)
        websockets.broadcast(CONNECTIONS, message)
        await websocket.wait_closed()
    except websockets.ConnectionClosed:
        CONNECTIONS.remove(websocket)
async def main():
    async with websockets.serve(Register, "192.168.1.56", 8000):
        await asyncio.get_running_loop().create_future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())