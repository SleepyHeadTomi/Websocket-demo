import websockets
import process_data
import asyncio

# create handler for each connection
async def handler(websocket):
    while True:
        try:
            data = await websocket.recv()
            response = await process_data.process_data(data)
            # reply = f"Data received as: {data}!"
            await websocket.send(response)
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed")
            break

start_server = websockets.serve(handler, "0.0.0.0", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()