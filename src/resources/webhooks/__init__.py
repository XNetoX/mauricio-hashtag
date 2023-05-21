from flask import Blueprint, Flask

from .views import payments_view

bp = Blueprint("webhooks", __name__, url_prefix="/webhooks")

bp.add_url_rule(
    rule="/payments", endpoint="payments", view_func=payments_view, methods=["POST"]
)


def register_in(app: Flask) -> None:
    app.register_blueprint(bp)
