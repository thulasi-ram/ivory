from django.urls import reverse
from marshmallow import Schema, fields

from common.schemas import AddressSchema
from user_profile.schemas import UserSchema


class LegalEntitySchema(Schema):
    uid = fields.String(required=True, dump_only=True)
    legal_name = fields.Str(required=True, dump_only=True)
    name = fields.String(required=True)
    business_type = fields.Str(required=True)
    gstin = fields.String(required=True)
    company_email = fields.Email(required=True)
    company_phone = fields.Str(required=True)
    notes = fields.String(required=True)
    address = fields.Nested(AddressSchema)
    admin_change_url = fields.Method('get_admin_change_url')
    view_url = fields.Method('get_view_url')

    def get_view_url(self, obj):
        return reverse('client_accounts:legal_entity', kwargs={'legal_entity_id': obj.uid})

    def get_admin_change_url(self, obj, **kwargs):
        return reverse('admin:client_accounts_legalentity_change', args=(obj.id,))


class ClientAddressSchema(Schema):
    line1 = fields.String(required=True, attribute='address.line1')
    line2 = fields.String(required=True, attribute='address.line2')
    city = fields.String(required=True, attribute='address.city')
    state = fields.String(required=True, attribute='address.state')
    country = fields.String(required=True, attribute='address.country')
    pincode = fields.String(required=True, attribute='address.pincode')
    address_type = fields.String(required=True)


class ClientAccountSchema(Schema):
    uid = fields.String(required=True, dump_only=True)
    legal_account = fields.Nested(LegalEntitySchema)
    name = fields.String(required=True)
    handled_by = fields.Nested(UserSchema)
    notes = fields.String(required=True)
    addresses = fields.Method('get_addresses')
    view_url = fields.Method('get_view_url')

    def get_addresses(self, obj):
        address_data, errors = ClientAddressSchema(many=True).dump(obj.addresses.all())
        return address_data

    def get_view_url(self, obj):
        return reverse('client_accounts:client', kwargs={'client_id': obj.uid})
