from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError

ma = Marshmallow()


def register_in(app: Flask) -> None:
    @app.errorhandler(ValidationError)
    def handle_marshmallow_validation(err):
        return jsonify(err.messages), 400

    ma.init_app(app)
