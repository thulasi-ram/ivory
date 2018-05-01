from marshmallow import Schema, fields


class UserProfileSchema(Schema):
    phone = fields.String(required=False)
    linkedin_url = fields.String(required=False)


class UserSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    profile = fields.Nested(UserProfileSchema)
