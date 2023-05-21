from flask import request
from sqlalchemy.exc import IntegrityError

from src.extensions.database import database
from src.resources.webhooks.models import Webhook
from src.resources.webhooks.schemas import webhook_schema
from src.resources.webhooks.services import payments_service


def payments_view():
    """
    Expected payload:
    {
        "nome": string,
        "email": string,
        "status": ("reembolsado", "aprovado", "recusado"),
        "valor":, float,
        "forma_pagamento": string,
        "parcelas": int
    }
    """

    payload = request.json
    treated_payload = webhook_schema.load(payload)

    webhook = Webhook(**treated_payload)
    database.session.add(webhook)
    database.session.commit()

    if payload["status"] == "aprovado":
        payments_service.send_welcome_message(webhook)
        payments_service.release_client_access(webhook)

    elif payload["status"] == "recusado":
        payments_service.send_payment_declined_message(webhook)

    elif payload["status"] == "reembolsado":
        payments_service.revoke_client_access(webhook)
        payments_service.send_refund_message(webhook)

    return {}, 204
