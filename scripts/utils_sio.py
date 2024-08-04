import asyncio
from src.log import server_log
import socketio

# Timeout for the socket.io connection (in seconds)
TIMEOUT = 5400  # secs

# Create an instance of the socket.io client
sio = socketio.AsyncClient()

@sio.event
async def connect(*args, **kwargs):
    server_log.info("Connected to Socket.IO server")
    # Start a timer to disconnect after TIMEOUT
    asyncio.get_event_loop().call_later(TIMEOUT, lambda: asyncio.create_task(sio.disconnect()))

@sio.event
async def disconnect():
    server_log.info("Disconnected from Socket.IO server")

@sio.on('*')
async def catch_all(event, data):
    server_log.info(f"Received event '{event}': {data}")
    if event == 'fin_busqueda':
        server_log.info(f"Final event received with data: {data}")
        await sio.disconnect()

def is_expected_format(data):
    return isinstance(data, dict) and 'status' in data

async def connect_to_sio():
    try:
        await sio.connect('http://localhost:9000/socket.io')
        await sio.wait()
    finally:
        await sio.disconnect()

def run_socketio():
    asyncio.run(connect_to_sio())
