from django.contrib import admin
from .models import CartModel


class CartModel1(admin.ModelAdmin):
    list_display = [
        'id',
        'pname',
        'price',
        'quantity',
        'totalprice',
        'get_username',
        'get_email'
    ]

    def get_username(self, obj):
        return obj.host.username
    get_username.short_description = 'Username'

    def get_email(self, obj):
        return obj.host.email
    get_email.short_description = 'Email'


admin.site.register(CartModel, CartModel1)
