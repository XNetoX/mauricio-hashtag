import logging
import os

from dotenv import load_dotenv

ROOT_DIR: str = os.path.dirname(os.path.abspath(__file__))
DOTENV_PATH: str = os.path.join(ROOT_DIR, ".env")
load_dotenv(DOTENV_PATH)


logger_message_format = "%(name)s:%(levelname)s:%(asctime)s:%(message)s"

logger_config = {
    "level": logging.INFO,
    "encoding": "utf-8",
    "format": logger_message_format,
}

REGISTER_TOKEN = os.environ.get("REGISTER_TOKEN")


class AppConfig:
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI: str = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_ECHO = True
    PROPAGATE_EXCEPTIONS: bool = True
    DEBUG: bool = os.environ.get("DEBUG")
    TESTING: bool = os.environ.get("TESTING")
    ENV: str = os.environ.get("ENV")
