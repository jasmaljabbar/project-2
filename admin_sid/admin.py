from django.contrib import admin
from .models import Category,Brand,Product

# Register your models here.

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('title')

# class BrandAdmin(admin.ModelAdmin):
#     list_display = ('title')

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title',
#                     'category',
#                     'brand',
#                     'image1',
#                     'image2',
#                     'image3',
#                     'image4',
#                     'description',
#                     'price',
#                     'old_price',
#                     'stock')
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
