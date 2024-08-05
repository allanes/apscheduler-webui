import os
from src.log import catalogo_vtex_log, server_log
import requests
from scripts.utils_catalogo_vtex.backend import iniciar_sincronizacion_catalogo
from scripts.utils_catalogo_vtex.sio import run_socketio, connect_to_sio

def funcion_prueba():
    print('Ejecutando funcion de prubea')
    catalogo_vtex_log.info('Ejecutando funcion de prubea')

def recibir_mensajes_progreso():
    if iniciar_sincronizacion_catalogo():
        catalogo_vtex_log.info("Iniciando conexion con SocketIO")
        # connect_to_sio()
        run_socketio()
    else:
        catalogo_vtex_log.error("Failed to trigger catalogo_vtex sync due to incorrect status code or missing token")
        server_log.error("Failed to trigger catalogo_vtex sync due to incorrect status code or missing token")

async def recibir_mensajes_progreso_async():
    if iniciar_sincronizacion_catalogo():
        catalogo_vtex_log.info("Iniciando conexion con SocketIO")
        await connect_to_sio()
    else:
        catalogo_vtex_log.error("Failed to trigger catalogo_vtex sync due to incorrect status code or missing token")
        server_log.error("Failed to trigger catalogo_vtex sync due to incorrect status code or missing token")


if __name__ == '__main__':
    # iniciar_sincronizacion_catalogo()
    recibir_mensajes_progreso()
