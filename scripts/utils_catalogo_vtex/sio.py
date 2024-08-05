import os
import asyncio
from src.log import catalogo_vtex_log, server_log
import socketio

# Timeout for the socket.io connection (in seconds)
TIMEOUT = 5400  # secs

# Create an instance of the socket.io client
sio = socketio.AsyncClient()

@sio.event
async def connect(*args, **kwargs):
    catalogo_vtex_log.info("Connected to Socket.IO server")
    # Start a timer to disconnect after TIMEOUT
    asyncio.get_event_loop().call_later(TIMEOUT, lambda: asyncio.create_task(sio.disconnect()))

@sio.event
async def disconnect():
    catalogo_vtex_log.info("Disconnected from Socket.IO server")

@sio.on('*')
async def catch_all(event, data):
    catalogo_vtex_log.info(f"Received event '{event}': {data}")
    if event == 'fin_busqueda':
        catalogo_vtex_log.info(f"Final event received with data: {data}")
        await sio.disconnect()

def is_expected_format(data):
    return isinstance(data, dict) and 'status' in data

async def connect_to_sio():
    try:
        domain = os.getenv('CATALOGO_VTEX_SIO_DOMAIN')
        port = os.getenv('CATALOGO_VTEX_SIO_PORT')  
        sio_url = f'http://{domain}:{port}'
        # sio_url = f'http://{domain}:{port}/socket.io'
        server_log.debug(f'URL de conexion SIO: {sio_url}')
        await sio.connect(sio_url)
        await sio.wait()
    # except Exception:
    #     catalogo_vtex_log.error(f'Error en la conexión con SocketIo')
    finally:
        await sio.disconnect()

def run_socketio():
    asyncio.run(connect_to_sio())
