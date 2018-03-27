from django.contrib import admin

# Register your models here.
from lead_management.models import Lead


class LeadAdmin(admin.ModelAdmin):
    readonly_fields = ('uid',)


admin.site.register(Lead, LeadAdmin)
