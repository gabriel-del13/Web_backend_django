from django.contrib import admin
from .models import Category, Product, Cart

# Register django rest framework 
admin.site.register(Category)
admin.site.register(Product)



#Only Read Cart
class ReadOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Cart, ReadOnlyAdmin)