from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Cart, CartItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','name', 'price', 'image_tag']
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image)
        return "-"
    image_tag.short_description = 'Image'

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)