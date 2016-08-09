from django.contrib import admin

from .models import PortalsAll
from .models import PortalClientsAll


admin.site.register(PortalsAll)
admin.site.register(PortalClientsAll)
