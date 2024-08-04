
from src.log import server_log
import socketio

# Create an instance of the socket.io client
sio = socketio.AsyncClient(logger=True, engineio_logger=True)

@sio.event
async def connect():
    server_log.info("Connected to Socket.IO server")

@sio.event
async def disconnect():
    server_log.info("Disconnected from Socket.IO server")

@sio.on('*')
async def catch_all(event, data):
    server_log.info(f"Received event '{event}': {data}")

async def connect_to_sio():
    try:
        await sio.connect('http://localhost:9000/socket.io')
        await sio.wait()
    except Exception as e:
        server_log.error(f"Failed to connect to Socket.IO server: {str(e)}")


