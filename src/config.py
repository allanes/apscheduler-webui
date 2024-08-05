import os
from pathlib import Path

from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

ROOT = Path(__file__).parent.parent
LOG_PATH = ROOT / "logs"

def get_db_url():
    domain = os.getenv('POSTGRES_CONTAINER_NAME')
    user = os.getenv('POSTGRES_USER')
    pswd = os.getenv('POSTGRES_PASSWORD')
    db = os.getenv('POSTGRES_DB')
    port = os.getenv('POSTGRES_PORT')
    
    db_url = f'postgresql://{user}:{pswd}@{domain}:{port}/{db}'
    # print(f'URL de conexion DB: {db_url}')
    # db_url = 'postgresql://adrian:1223@catalogo-vtex-scheduler-db:5432/scheduler-db-2'
    return db_url

SCHEDULER_CONFIG = {
    "executors": {"default": AsyncIOExecutor()},
    "jobstores": {"postgres": SQLAlchemyJobStore(
        url=get_db_url()
    )},
}
