from rest_framework import serializers
from .models import Favorites
from products.serializers import ProductSerializer
from products.models import Product

class FavoritesSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = Favorites
        fields = ['id', 'user', 'product', 'product_id', 'created_at', 'updated_at']