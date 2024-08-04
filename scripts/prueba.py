import os
from src.log import server_log
import requests
import httpx
import asyncio
from scripts.utils_sio import run_socketio#, connect_to_sio

def funcion_prueba():
    print('Ejecutando funcion de prubea')
    server_log.info('Ejecutando funcion de prubea')

def iniciar_sincronizacion_catalogo() -> bool:
    server_log.info('Ejecutando sincronizacion de catalogo vtex...')
    domain = 'localhost'
    port = '9000'
    base_url = f'http://{domain}:{port}/api'
    url = f'{base_url}/salidas/start-fetch-products'
    token = os.getenv("API_TOKEN")
    headers = {'Authorization': f'Bearer {token}'}
    params = {'verificar_links': False, 'completo': False}
    
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        server_log.info("Successfully triggered catalogo_vtex sync")
        return True
    else:
        server_log.error(f"Failed to trigger catalogo_vtex sync. Status code: {response.status_code}")
        return False

def recibir_mensajes_progreso():
    if iniciar_sincronizacion_catalogo():
        server_log.info("Iniciando conexion con SocketIO")
        # connect_to_sio()
        run_socketio()
    else:
        server_log.error("Failed to trigger catalogo_vtex sync due to incorrect status code or missing token")

if __name__ == '__main__':
    iniciar_sincronizacion_catalogo()
    recibir_mensajes_progreso()
