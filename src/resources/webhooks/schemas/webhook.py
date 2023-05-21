from marshmallow import Schema, fields, validate, post_dump

from src.resources.webhooks.models.webhook import PaymentStatusConstraint
from .system_action import SystemActionSchema


class WebhookSchema(Schema):
    id = fields.String(required=True, dump_only=True)
    name = fields.String(data_key="nome", required=True)
    email = fields.String(data_key="email", required=True)
    status = fields.String(
        data_key="status",
        required=True,
        validate=[
            validate.OneOf([status.value for status in PaymentStatusConstraint]),
        ],
    )
    value = fields.Number(data_key="valor", required=True)
    payment_method = fields.String(data_key="forma_pagamento", required=True)
    installments = fields.Integer(data_key="parcelas", required=True)

    actions = fields.Nested(SystemActionSchema, many=True, dump_only=True)

    @post_dump
    def process_data(self, data, *args, **kwargs):
        data["status"] = data["status"].split(".")[-1]
        return data


webhook_schema = WebhookSchema()
