from django.contrib import admin
from contact.models import *


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
       list_display = ['name']
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
       list_display = ['phone', 'country']
