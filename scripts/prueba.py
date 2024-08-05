import os
from src.log import catalogo_vtex_log, server_log
import requests
from scripts.utils_sio import run_socketio#, connect_to_sio

def funcion_prueba():
    print('Ejecutando funcion de prubea')
    catalogo_vtex_log.info('Ejecutando funcion de prubea')

def iniciar_sincronizacion_catalogo() -> bool:
    catalogo_vtex_log.info('Ejecutando sincronizacion de catalogo vtex...')
    # domain = 'localhost'
    # port = '9000'
    # base_url = f'http://{domain}:{port}/api'
    domain = 'catalogovtex_backend'
    port = '5000'
    base_url = f'http://{domain}:{port}'
    url = f'{base_url}/salidas/start-fetch-products'
    token = os.getenv("API_TOKEN")
    headers = {'Authorization': f'Bearer {token}'}
    params = {'verificar_links': False, 'completo': False}
    
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        catalogo_vtex_log.info("Successfully triggered catalogo_vtex sync")
        server_log.info("Successfully triggered catalogo_vtex sync")
        return True
    else:
        catalogo_vtex_log.error(f"Failed to trigger catalogo_vtex sync. Status code: {response.status_code}")
        server_log.error(f"Failed to trigger catalogo_vtex sync. Status code: {response.status_code}")
        return False

def recibir_mensajes_progreso():
    if iniciar_sincronizacion_catalogo():
        catalogo_vtex_log.info("Iniciando conexion con SocketIO")
        # connect_to_sio()
        run_socketio()
    else:
        catalogo_vtex_log.error("Failed to trigger catalogo_vtex sync due to incorrect status code or missing token")
        server_log.error("Failed to trigger catalogo_vtex sync due to incorrect status code or missing token")

if __name__ == '__main__':
    iniciar_sincronizacion_catalogo()
    recibir_mensajes_progreso()
