from dal import autocomplete
from django.contrib import admin
# Register your models here.
from django.forms import ModelForm, ModelChoiceField

from client_accounts.models import Contact
from lead_management.models import Lead


class LeadForm(ModelForm):
    contact = ModelChoiceField(
        queryset=Contact.objects.all(),
        widget=autocomplete.ModelSelect2(url='client_accounts:contact-autocomplete'))

    class Meta:
        model = Lead
        fields = ('__all__')


class LeadAdmin(admin.ModelAdmin):
    form = LeadForm
    readonly_fields = ('uid',)
    list_display = ('uid', 'contact', 'stage')


admin.site.register(Lead, LeadAdmin)
