from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def register_in(app: Flask) -> None:
    bootstrap.init_app(app)
