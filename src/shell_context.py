from src.extensions.database import database
from src.resources.webhooks.models import SystemAction, Webhook
from src.resources.webhooks.schemas import system_action_schema, webhook_schema


def get_shell_context() -> dict:
    return {
        "session": database.session,
        "Webhook": Webhook,
        "SystemAction": SystemAction,
        "webhook_schema": webhook_schema,
        "system_action_schema": system_action_schema,
    }
