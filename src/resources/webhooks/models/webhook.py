from enum import Enum

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.extensions.database import database


class PaymentStatusConstraint(Enum):
    reembolsado = "reembolsado"
    aprovado = "aprovado"
    recusado = "recusado"


class Webhook(database.Model):
    __tablename__ = "webhooks"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100), nullable=False)
    email = sa.Column(sa.String(200), nullable=False)
    status = sa.Column(sa.Enum(PaymentStatusConstraint), nullable=False)
    value = sa.Column(sa.Numeric, nullable=False)
    payment_method = sa.Column(sa.String(100), nullable=False)
    installments = sa.Column(sa.Integer, nullable=False)

    actions = relationship("SystemAction", back_populates="webhook")
