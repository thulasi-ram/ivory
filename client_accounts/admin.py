from dal import autocomplete
from django.contrib import admin
# Register your models here.
from django.core.exceptions import ValidationError
from django.forms import ModelForm, ModelChoiceField, BaseInlineFormSet

from client_accounts.models import LegalEntity, ClientAccount, ClientAccountAddresses, BusinessType
from common.models import Address
from user_profile.models import User


class ClientAccountAddressInlineFormset(BaseInlineFormSet):
    address = ModelChoiceField(
        queryset=Address.objects.all(),
        widget=autocomplete.ModelSelect2(url='client_accounts:address-autocomplete'))

    def clean(self):
        super().clean()
        for form in self.forms:
            if not hasattr(form, 'cleaned_data'):
                continue
            data = form.cleaned_data
            address_type = data.get('address_type')

            if not address_type:
                raise ValidationError('Address type is required')


class ClientAccountAddressInline(admin.TabularInline):
    model = ClientAccountAddresses
    formset = ClientAccountAddressInlineFormset
    fields = ['address', 'address_type']
    extra = 0
    min_num = 1


class ClientAccountForm(ModelForm):
    handled_by = ModelChoiceField(
        queryset=User.objects.all(),
        widget=autocomplete.ModelSelect2(url='user_profile:user-autocomplete'))

    legal_account = ModelChoiceField(
        queryset=LegalEntity.objects.all(),
        widget=autocomplete.ModelSelect2(url='client_accounts:legal-entity-autocomplete'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = ClientAccount
        fields = ('__all__')


class ClientAccountAdmin(admin.ModelAdmin):
    form = ClientAccountForm
    inlines = [ClientAccountAddressInline]
    readonly_fields = ['uid', 'created_by']
    search_fields = ['uid', 'name', 'legal_account__name']
    list_display = ['uid', 'name', 'legal_account', 'handled_by']


class LegalEntityForm(ModelForm):
    address = ModelChoiceField(
        queryset=Address.objects.all(),
        widget=autocomplete.ModelSelect2(url='client_accounts:address-autocomplete'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = LegalEntity
        fields = ('__all__')


class LegalEntityAdmin(admin.ModelAdmin):
    form = LegalEntityForm
    readonly_fields = ['uid', 'created_by']
    search_fields = ['uid', 'legal_name', 'company_email', 'company_phone', 'gstin']
    list_display = ['uid', 'legal_name', 'company_email', 'company_phone', 'gstin']


admin.site.register(LegalEntity, LegalEntityAdmin)
admin.site.register(ClientAccount, ClientAccountAdmin)
admin.site.register(BusinessType)
