from flask import Blueprint, Flask

from .views import login, register

bp = Blueprint(
    "authentication",
    __name__,
    url_prefix="/auth",
    template_folder="templates",
    static_folder="static",
)

bp.add_url_rule(
    rule="/login",
    endpoint="login",
    view_func=login,
    methods=["POST", "GET"],
)

bp.add_url_rule(
    rule="/register",
    endpoint="register",
    view_func=register,
    methods=["POST", "GET"],
)


def register_in(app: Flask) -> None:
    app.register_blueprint(bp)
