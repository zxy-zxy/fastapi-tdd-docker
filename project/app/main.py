import os
import logging
from logging import config

from fastapi import FastAPI

from app.api import ping, summaries
from app.db import init_db

logging_config_filepath = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "logging.ini"
)
logging.config.fileConfig(logging_config_filepath, disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(summaries.router, prefix="/summaries", tags=["summaries"])

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
