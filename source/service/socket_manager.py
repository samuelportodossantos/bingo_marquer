import asyncio
import websockets
import json

class SocketManager:

    def __init__(self):
        self.clients = set()

    async def handler(self, websocket):
        self.clients.add(websocket)
        try:
            async for message in websocket:
                data = json.loads(message)
                print(f"Received: {data}")
                response = json.dumps({"status": "received"})
                await websocket.send(response)
        finally:
            self.clients.remove(websocket)

    async def broadcast(self, message):

        print(f"Enviando para {len(self.clients)} clientes...")
        if self.clients: 
            await asyncio.gather(*[client.send(message) for client in self.clients])


    async def start_server(self):
        async with websockets.serve(self.handler, "0.0.0.0", 5001):
            await asyncio.Future()
