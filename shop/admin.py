from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    product_display = ('id', 'title', 'is_published',
                       'price', 'product_date',)
    product_display_links = ('id', 'title')
    product_editable = ('in_stock',)
    list_per_page = 25


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
