from django.urls import reverse
from marshmallow import Schema, fields


class UserProfileSchema(Schema):
    phone = fields.String(required=False)
    linkedin_url = fields.String(required=False)


class UserSchema(Schema):
    username = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    full_name = fields.String(attribute='get_full_name')
    email = fields.Email(required=True)
    profile = fields.Nested(UserProfileSchema)
    view_url = fields.Method('get_view_url')

    def get_view_url(self, obj):
        return reverse('user_profile:user-profile', kwargs={'username': obj.username})
