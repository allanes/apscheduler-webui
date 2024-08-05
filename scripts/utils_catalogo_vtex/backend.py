import os
from src.log import catalogo_vtex_log, server_log
import requests

def iniciar_sincronizacion_catalogo() -> bool:
    catalogo_vtex_log.info('Ejecutando sincronizacion de catalogo vtex...')
    domain = os.getenv('CATALOGO_VTEX_BACKEND_DOMAIN')
    port = os.getenv('CATALOGO_VTEX_BACKEND_PORT')
    base_url = f'http://{domain}:{port}'
    url = f'{base_url}/salidas/start-fetch-products'
    server_log.info(f'URL de conexion BACKEND: {url}')
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