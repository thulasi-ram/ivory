from dal import autocomplete
from django.contrib import admin
# Register your models here.
from django.forms import ModelForm, ModelChoiceField

from client_accounts.models import ClientAccount
from lead_management.models import Lead, LeadStage, Designation
from user_profile.models import User


class LeadForm(ModelForm):
    client_account = ModelChoiceField(
        queryset=ClientAccount.objects.all(),
        widget=autocomplete.ModelSelect2(url='client_accounts:client-account-autocomplete'))
    contact = ModelChoiceField(
        queryset=User.objects.all(),
        widget=autocomplete.ModelSelect2(url='user_profile:user-autocomplete'))

    class Meta:
        model = Lead
        fields = ('__all__')


class LeadAdmin(admin.ModelAdmin):
    form = LeadForm
    readonly_fields = ('uid',)
    list_display = ('uid', 'client_account', 'contact', 'stage')


admin.site.register(Lead, LeadAdmin)
admin.site.register(LeadStage)
admin.site.register(Designation)
