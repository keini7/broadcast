import asyncio
import websockets
from utils import generate_client_id

PORT = 8765
URI = f"ws://localhost:{PORT}"

async def listen(ws):
    try:
        async for message in ws:
            print(f"\n{message}")
    except websockets.exceptions.ConnectionClosed:
        print("Disconnected from server.")

async def send(ws, client_id):
    while True:
        msg = input("You: ")
        if msg.lower() == "/quit":
            print("Disconnecting...")
            break
        await ws.send(f"{client_id}|{msg}")

async def main():
    client_id = generate_client_id()
    print(f"Connected as client ID: {client_id}")
    try:
        async with websockets.connect(URI) as ws:
            await asyncio.gather(
                listen(ws),
                send(ws, client_id)
            )
    except ConnectionRefusedError:
        print("Connection failed. Is the server running?")

if __name__ == "__main__":
    asyncio.run(main())
