import logging
from typing import List

from src.extensions.database import database
from src.resources.webhooks.models import Webhook
from src.resources.webhooks.schemas import webhook_schema

logger = logging.getLogger(__name__)


def get_all_webhooks() -> List[dict]:
    webhooks: List[Webhook] = database.session.query(Webhook).all()
    return webhook_schema.dump(webhooks, many=True)


def get_webhooks_by_email(email: str) -> List[dict]:
    webhooks: List[Webhook] = (
        database.session.query(Webhook).filter_by(email=email).all()
    )
    if webhooks:
        return webhook_schema.dump(webhooks, many=True)
    else:
        return [{}]
