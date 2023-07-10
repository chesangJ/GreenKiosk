from django.contrib import admin

# Register your models here.

from .models import Cart
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display=("product","image","quantity","price")
admin.site.register(Cart,CartAdmin)