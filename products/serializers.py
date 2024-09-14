from rest_framework import serializers
from .models import Category, Product, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    parent_category = serializers.StringRelatedField()
    class Meta:
        model = Category
        fields = ['id', 'name_category','parent_category', 'created_at', 'updated_at']

class ProductImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image_url']
        ref_name = 'FavoritesProductImageSerializer'


    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name_product', 'description', 'price', 'available_quantity', 
                  'images', 'category', 'category_id', 'status', 'created_at', 'updated_at']
