from django.contrib import admin

# Register your models here.
from client_accounts.models import LegalEntity, ClientAccount, Contact

admin.site.register(LegalEntity)
admin.site.register(ClientAccount)
admin.site.register(Contact)