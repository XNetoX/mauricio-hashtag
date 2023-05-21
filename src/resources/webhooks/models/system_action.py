from enum import Enum

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.extensions.database import database


class ActionConstraint(Enum):
    access_released = "access_released"
    access_revoked = "access_revoked"
    welcome_message = "welcome_message"
    payment_declined_message = "payment_declined_message"
    refund_message = "refund_message"


class SystemAction(database.Model):
    __tablename__ = "system_actions"

    id = sa.Column(sa.Integer, primary_key=True)
    action = sa.Column(sa.Enum(ActionConstraint), nullable=False)
    action_time = sa.Column(sa.DateTime, nullable=False)

    webhook_id = sa.Column(sa.Integer, sa.ForeignKey("webhooks.id"))

    webhook = relationship("Webhook", back_populates="actions")
