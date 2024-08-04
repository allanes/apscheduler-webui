import os
from src.log import server_log
import requests
# from scripts.utils_logging import logger

def funcion_prueba():
    print('Ejecutando funcion de prubea')
    server_log.info('Ejecutando funcion de prubea')

def iniciar_sincronizacion_catalogo():
    server_log.info('Ejecutando sincronizacion de catalogo vtex...')
    domain = 'localhost'
    port = '9000'
    base_url = f'http://{domain}:{port}/api'
    url = f'{base_url}/salidas/start-fetch-products'
    token = os.getenv("API_TOKEN")
    if not token:
        # logger.error("API_TOKEN is not set in environment variables")
        # last_sync_status = {"timestamp": datetime.now(), "status": "Failed - API_TOKEN not set"}
        return

    headers = {'Authorization': f'Bearer {token}'}
    params = {
        'verificar_links': False,
        'completo': False
    }
    server_log.info(f'    Ejecutando consulta...')
    response = requests.get(
        url=url,
        params=params,
        headers=headers
    )
    if response.status_code == 200:
        # print("Successfully triggered catalogo_vtex sync")
        server_log.info("Successfully triggered catalogo_vtex sync")
        # last_sync_status = {"timestamp": datetime.now(), "status": "Success"}
    else:
        # print(f"Failed to trigger catalogo_vtex sync. Status code: {response.status_code}")
        server_log.error(f"Failed to trigger catalogo_vtex sync. Status code: {response.status_code}")
        # last_sync_status = {"timestamp": datetime.now(), "status": f"Failed - Status code: {response.status_code}"}

if __name__ == '__main__':
    iniciar_sincronizacion_catalogo()