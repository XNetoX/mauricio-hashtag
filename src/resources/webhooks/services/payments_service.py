import logging
from datetime import datetime

from src.extensions.database import database
from src.resources.webhooks.models import SystemAction, Webhook

logger = logging.getLogger(__name__)


def send_welcome_message(webhook: Webhook) -> None:
    # mandar mensagem de boas vindas para o cliente

    logger.info(
        "welcome_message_sent_to_customer",
        extra={"client_name": webhook.name, "client_email": webhook.email},
    )
    action = SystemAction(
        action="welcome_message",
        action_time=datetime.utcnow(),
        webhook_id=webhook.id,
    )

    database.session.add(action)
    database.session.commit()


def release_client_access(webhook: Webhook) -> None:
    # liberar acesso do cliente

    logger.info(
        "client_access_released",
        extra={"client_name": webhook.name, "client_email": webhook.email},
    )

    action = SystemAction(
        action="access_released",
        action_time=datetime.utcnow(),
        webhook_id=webhook.id,
    )

    database.session.add(action)
    database.session.commit()


def send_payment_declined_message(webhook: Webhook) -> None:
    # mandar mensagem de pagamente recusado para o cliente

    logger.info(
        "payment_declined_message_sent_to_customer",
        extra={"client_name": webhook.name, "client_email": webhook.email},
    )

    action = SystemAction(
        action="payment_declined_message",
        action_time=datetime.utcnow(),
        webhook_id=webhook.id,
    )

    database.session.add(action)
    database.session.commit()


def revoke_client_access(webhook: Webhook) -> None:
    # retirada do accesso ao curso do usuário

    logger.info(
        "client_access_revoked",
        extra={"client_name": webhook.name, "client_email": webhook.email},
    )

    action = SystemAction(
        action="access_revoked",
        action_time=datetime.utcnow(),
        webhook_id=webhook.id,
    )

    database.session.add(action)
    database.session.commit()


def send_refund_message(webhook: Webhook) -> None:
    # enviar mensagem de reembolso para o cliente

    logger.info(
        "refund_message_sent_to_customer",
        extra={"client_name": webhook.name, "client_email": webhook.email},
    )

    action = SystemAction(
        action="refund_message",
        action_time=datetime.utcnow(),
        webhook_id=webhook.id,
    )

    database.session.add(action)
    database.session.commit()
