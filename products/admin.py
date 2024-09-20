from django.contrib import admin
from .models import ChildCategory, ParentCategory, Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(ProductImage)
admin.site.register(ChildCategory)
admin.site.register(ParentCategory)