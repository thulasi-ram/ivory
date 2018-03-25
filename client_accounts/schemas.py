from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    created_at = fields.DateTime(required=True)


class LegalEntitySchema(Schema):
    name = fields.Str(required=True)
    business_type = fields.Str(required=True)
    gstin = fields.Str(required=True)
    company_email = fields.Email(required=True)
    company_phone = fields.Str(required=True)
    notes = fields.Str(required=True)
    created_by = fields.Nested(UserSchema)
