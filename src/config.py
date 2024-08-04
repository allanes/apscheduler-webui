from pathlib import Path

from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

ROOT = Path(__file__).parent.parent
LOG_PATH = ROOT / "logs"

SCHEDULER_CONFIG = {
    "executors": {"default": AsyncIOExecutor()},
    "jobstores": {"postgres": SQLAlchemyJobStore(
        url='postgresql://adrian:1223@localhost:5432/scheduler-db'
    )},
}
