from rest_framework import serializers
from .models import ChildCategory, ParentCategory, Product, ProductImage

class ParentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentCategory
        fields = ['id', 'name_parentcategory', 'created_at', 'updated_at']


class ChildCategorySerializer(serializers.ModelSerializer):
    parent_category = serializers.StringRelatedField()  # Para mostrar el nombre de la parent_category
    
    class Meta:
        model = ChildCategory
        fields = ['id', 'name_childcategory', 'parent_category', 'created_at', 'updated_at']



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
    child_category = ChildCategorySerializer(read_only=True)
    child_category_id = serializers.PrimaryKeyRelatedField(
        queryset=ChildCategory.objects.all(), source='child_category', write_only=True
    )
    parent_category = serializers.StringRelatedField(read_only=True)  # Para mostrar el nombre de la parent_category
    parent_category_id = serializers.PrimaryKeyRelatedField(
        queryset=ParentCategory.objects.all(), source='parent_category', write_only=True, required=False
    )
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name_product', 'description', 'price', 'available_quantity', 
                  'images', 'child_category', 'child_category_id', 'parent_category', 'parent_category_id',
                  'status', 'created_at', 'updated_at']
