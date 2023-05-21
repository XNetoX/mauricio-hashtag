from flask import Blueprint, Flask

from .views import home

bp = Blueprint(
    "home",
    __name__,
    url_prefix="/",
    template_folder="templates",
    static_folder="static",
)

bp.add_url_rule(rule="/", endpoint="home", view_func=home, methods=["GET", "POST"])


def register_in(app: Flask) -> None:
    app.register_blueprint(bp)
