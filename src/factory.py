import logging

from flask import Flask

from config import AppConfig, logger_config
from src.extensions import database, serializer, frontend
from src.resources import authentication, health_check, home, webhooks
from src.shell_context import get_shell_context

logging.basicConfig(**logger_config)


def register_views(app:Flask) -> None:
    health_check.register_in(app)
    webhooks.register_in(app)
    authentication.register_in(app)
    home.register_in(app)


def register_extensions(app:Flask) -> None:
    database.register_in(app)
    create_database(app)
    serializer.register_in(app)
    frontend.register_in(app)

def create_database(app:Flask) -> None:
    with app.app_context():
        database.database.create_all()


def create_app(config: AppConfig) -> Flask:
    app = Flask(__name__)

    app.config.from_object(config)
    app.shell_context_processor(get_shell_context)

    register_extensions(app)
    register_views(app)

    return app
