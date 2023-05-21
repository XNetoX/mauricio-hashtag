from datetime import datetime
from marshmallow import Schema, fields, validate, post_dump

from src.resources.webhooks.models.system_action import ActionConstraint


class SystemActionSchema(Schema):
    id = fields.String(required=True, dump_only=True)
    action = fields.String(
        required=True,
        validate=[
            validate.OneOf([status.value for status in ActionConstraint]),
        ],
    )
    action_time = fields.DateTime(required=True)
    webhook_id = fields.Number(required=True)

    @post_dump
    def process_data(self, data, *args, **kwargs):
        data["action"] = data["action"].split(".")[-1]
        data["action_time"] = datetime.strptime(
            data["action_time"], "%Y-%m-%dT%H:%M:%S.%f"
        ).strftime("%Y-%m-%d %H:%M:%S")
        return data


system_action_schema = SystemActionSchema()
