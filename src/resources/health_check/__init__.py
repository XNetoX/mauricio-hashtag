from flask import Blueprint, Flask

from .views import info_view

bp = Blueprint("health_check", __name__, url_prefix="/health_check")

bp.add_url_rule(rule="/info", endpoint="info", view_func=info_view, methods=["GET"])


def register_in(app: Flask) -> None:
    app.register_blueprint(bp)
