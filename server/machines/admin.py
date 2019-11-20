from django.contrib import admin
from .models import Machine

class MachineAdmin(admin.ModelAdmin):
    list_display = ('ee_tag', 'owner', 'alias', 'description', 'ip', 'updated')
    list_filter = ['updated']
    search_fields = ['ee_tag', 'owner', 'alias']

admin.site.register(Machine, MachineAdmin)
