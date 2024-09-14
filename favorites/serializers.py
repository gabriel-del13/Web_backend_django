from rest_framework import serializers
from .models import Favorites
from products.models import ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']
        ref_name = 'ProductsProductImageSerializer'


class FavoritesSerializer(serializers.ModelSerializer):
    name_product = serializers.CharField(read_only=True)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    available_quantity = serializers.IntegerField(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    category = serializers.CharField(source='category.name_category', read_only=True)
    status = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)

    class Meta:
        model = Favorites
        fields = ['id', 'user', 'product', 'name_product', 'price', 'available_quantity', 'images',
                  'category', 'status', 'description', 'created_at', 'updated_at']
        
        read_only_fields = ['name_product', 'price', 'available_quantity', 'images', 'category', 'status', 'description']