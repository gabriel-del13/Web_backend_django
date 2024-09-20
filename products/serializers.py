from rest_framework import serializers
from .models import Category, Product, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    parent_category = serializers.StringRelatedField()  # Para mostrar el nombre de la parent_category
    subcategories = serializers.SerializerMethodField()  # Campo adicional para subcategorías

    class Meta:
        model = Category
        fields = ['id', 'name_category', 'parent_category', 'subcategories', 'created_at', 'updated_at']

    def get_subcategories(self, obj):
        # Obtener las subcategorías relacionadas con esta categoría
        subcategories = obj.subcategories.all()  # Usa el related_name "subcategories" que tienes en el modelo
        return CategorySerializer(subcategories, many=True).data


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
