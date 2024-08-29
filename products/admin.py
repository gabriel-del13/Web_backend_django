from django.contrib import admin
from .models import Category, Product, ProductImage, Cart

# Register django rest framework 
class ProducImageInline(admin.TabularInline):
    model =  ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProducImageInline]
    
admin.site.register(ProductImage)

#Product
admin.site.register(Category)



#Only Read Cart
class ReadOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Cart, ReadOnlyAdmin)