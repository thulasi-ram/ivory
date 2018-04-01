from marshmallow import Schema, fields

from client_accounts.schemas import ContactSchema


class LeadSchema(Schema):
    uid = fields.String(required=True, dump_only=True)
    stage = fields.String(required=True)
    contact = fields.Nested(ContactSchema)
