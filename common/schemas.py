from marshmallow import Schema, fields


class AddressSchema(Schema):
    line1 = fields.String(required=True)
    line2 = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)
    country = fields.String(required=True)
    pincode = fields.String(required=True)
