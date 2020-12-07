import os
import logging
from logging import config

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api import ping

logging_config_filepath = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "logging.ini"
)
logging.config.fileConfig(logging_config_filepath, disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()

    register_tortoise(
        application,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

    application.include_router(ping.router)

    return application


app = create_application()
