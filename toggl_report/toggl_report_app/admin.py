from django.contrib import admin

# Register your models here.

from .models import TogglUser

class TogglUserAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, {'fields': ['user_id']}),
                 ('API_TOKEN', {'fields': ['api_token']}),
                 ]
    list_filter = ['user_id']
    search_fields = ['user_id']

admin.site.register(TogglUser, TogglUserAdmin)
