import sqlalchemy as sa

from src.extensions.database import database


class User(database.Model):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String(200), nullable=False, unique=True)
    password_hash = sa.Column(sa.String, nullable=False)
