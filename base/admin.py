
from django.contrib import admin
from .models import Products, Update

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'pname', 'pcategory']

admin.site.register(Products, ProductAdmin)
admin.site.register(Update)

