from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

migrate = Migrate()


def register_in(app) -> None:
    database.init_app(app)
    app.database = database
    migrate.init_app(app, database)
