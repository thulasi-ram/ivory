from marshmallow import Schema, fields

from client_accounts.schemas import ClientAccountSchema
from user_profile.schemas import UserSchema


class LeadSchema(Schema):
    uid = fields.String(required=True, dump_only=True)
    stage = fields.String(required=True)
    client_account = fields.Nested(ClientAccountSchema)
    contact = fields.Nested(UserSchema)
    designation = fields.String(required=True)
    notes = fields.String(required=True)
