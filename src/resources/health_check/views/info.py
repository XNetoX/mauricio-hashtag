import sys

from flask import jsonify


def info_view():
    return jsonify(
        {
            "app": "payments webhook",
            "pythonVersion": str(sys.version),
            "versionInfo": str(sys.version_info),
        }
    )
