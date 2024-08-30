from django.contrib import admin

from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

class ReadOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Cart)
class CartAdmin(ReadOnlyAdmin):
    inlines = [CartItemInline]
    list_display = ['user', 'status', 'created_at', 'updated_at']
    list_filter = ['status']
    search_fields = ['user__username', 'user__email']