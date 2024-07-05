from django.contrib import admin
from .models import *


class UserOrderModelAdmin(admin.ModelAdmin):
    list_display = ('card_number', 'owner_name', 'email')
    search_fields = ('owner_name', 'email', 'phone_number')


admin.site.register(UserOrderModel, UserOrderModelAdmin)
