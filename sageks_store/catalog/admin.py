from django.contrib import admin

from .models import *


class ProductImagesInline(admin.StackedInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price', 'stock', 'available']
    list_filter = ['available']
    list_editable = ['price', 'stock', 'available']
    inlines = [ProductImagesInline]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
