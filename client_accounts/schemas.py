from django.urls import reverse
from marshmallow import Schema, fields


class UserProfileSchema(Schema):
    phone = fields.String(required=False)
    linkedin_url = fields.URL(required=False, default='')


class UserSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    profile = fields.Nested(UserProfileSchema)


class AddressSchema(Schema):
    line1 = fields.String(required=True)
    line2 = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)
    country = fields.String(required=True)
    pincode = fields.String(required=True)
    address_type = fields.String(required=True)


class LegalEntitySchema(Schema):
    uid = fields.String(required=True, dump_only=True)
    legal_name = fields.Str(required=True, dump_only=True)
    name = fields.String(required=True)
    business_type = fields.Str(required=True)
    gstin = fields.String(required=True)
    company_email = fields.Email(required=True)
    company_phone = fields.Str(required=True)
    notes = fields.String(required=True)
    addresses = fields.Nested(AddressSchema)
    admin_change_url = fields.Method('get_admin_change_url')

    def get_admin_change_url(self, obj, **kwargs):
        return reverse('admin:client_accounts_legalentity_change', args=(obj.id,))


class ClientAccountSchema(Schema):
    uid = fields.String(required=True, dump_only=True)
    legal_account = fields.Nested(LegalEntitySchema)
    name = fields.String(required=True)
    handled_by = fields.Nested(UserSchema)
    notes = fields.String(required=True)


class ContactSchema(Schema):
    client_account = fields.Nested(ClientAccountSchema)
    user = fields.Nested(UserSchema)
    designation = fields.String(required=True)
    notes = fields.String(required=True)
