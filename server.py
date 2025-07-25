import asyncio
import websockets
from utils import format_message
import os

PORT = 8765
connected_clients = set()
CHAT_LOG = "chat.log"

async def send_chat_history(websocket):
    if os.path.exists(CHAT_LOG):
        with open(CHAT_LOG, "r") as f:
            for line in f:
                try:
                    await websocket.send(line.strip())
                except:
                    pass

async def handler(websocket):
    print("Client connected")
    connected_clients.add(websocket)
    await send_chat_history(websocket)

    try:
        async for message in websocket:
            try:
                sender_id, content = message.split("|", 1)
            except ValueError:
                sender_id, content = "Unknown", message

            formatted = format_message(sender_id, content)

            with open(CHAT_LOG, "a") as f:
                f.write(formatted + "\n")

            await broadcast(formatted, websocket)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        connected_clients.remove(websocket)

async def broadcast(message, sender):
    for client in connected_clients:
        if client != sender:
            try:
                await client.send(message)
            except:
                pass

async def main():
    async with websockets.serve(handler, "localhost", PORT):
        print(f"Server running on ws://localhost:{PORT}")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
