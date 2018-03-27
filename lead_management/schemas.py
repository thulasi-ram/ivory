from marshmallow import Schema, fields

from client_accounts.schemas import ClientAccountSchema, UserSchema


class LeadSchema(Schema):
    uid = fields.String(required=True, dump_only=True)
    client_account = fields.Nested(ClientAccountSchema)
    stage = fields.String(required=True)
    contact = fields.Nested(UserSchema)
