from rest_framework import serializers
from .models import ChildCategory, ParentCategory, Product, ProductImage




class ChildCategorySerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo ChildCategory. 

    Este serializador transforma las instancias del modelo ChildCategory en un formato JSON adecuado para la API.
    También se utiliza para deserializar los datos JSON en instancias del modelo ChildCategory.

    Atributos:
        parent_category (StringRelatedField): Campo de solo lectura que muestra el nombre de la categoría principal (ParentCategory).
    """
    parent_category = serializers.StringRelatedField(help_text="Nombre de la categoría principal asociada a esta subcategoría.")

    class Meta:
        model = ChildCategory
        fields = ['id', 'name_childcategory', 'parent_category', 'created_at', 'updated_at']
        extra_kwargs = {
            'created_at': {'help_text': 'Fecha y hora de creación de la subcategoría.'},
            'updated_at': {'help_text': 'Fecha y hora de la última actualización de la subcategoría.'},
        }
        
        
class ParentCategorySerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo ParentCategory.

    Este serializador transforma las instancias del modelo ParentCategory en un formato JSON adecuado para la API.
    También incluye un campo personalizado para listar las subcategorías asociadas a la categoría principal.

    Atributos:
        subcategories (SerializerMethodField): Campo de solo lectura que devuelve las subcategorías (ChildCategory) asociadas a esta categoría principal.
    """
    
    subcategories = serializers.SerializerMethodField(help_text="Lista de subcategorías (ChildCategory) asociadas a esta categoría principal.")
    
    class Meta:
        model = ParentCategory
        fields = ['id', 'name_parentcategory', 'subcategories', 'created_at', 'updated_at']
        extra_kwargs = {
            'created_at': {'help_text': 'Fecha y hora de creación de la categoría principal.'},
            'updated_at': {'help_text': 'Fecha y hora de la última actualización de la categoría principal.'},
        }

    def get_subcategories(self, obj):
        """
        Devuelve una lista de subcategorías asociadas a la categoría principal.
        
        La lista contiene solo el 'id' y 'name_childcategory' de las subcategorías.
        """
        return obj.subcategories.values('id', 'name_childcategory')
    
    
class ProductImageSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo ProductImage.

    Este serializador transforma las instancias del modelo ProductImage en un formato JSON adecuado para la API,
    incluyendo un campo personalizado para devolver la URL completa de la imagen.
    
    Atributos:
        image_url (SerializerMethodField): Campo de solo lectura que devuelve la URL absoluta de la imagen.
    """
    
    image_url = serializers.SerializerMethodField(help_text="URL absoluta de la imagen del producto.")
    
    class Meta:
        model = ProductImage
        fields = ['id', 'image_url']
        ref_name = 'FavoritesProductImageSerializer'  # Nombre de referencia para evitar conflictos en Swagger cuando se usan múltiples serializadores relacionados con imágenes.
    
    def get_image_url(self, obj):
        """
        Devuelve la URL absoluta de la imagen del producto.

        Si la imagen está presente, se genera la URL completa utilizando el objeto request.
        """
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
    

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Product.

    Este serializador transforma las instancias del modelo Product en un formato JSON adecuado para la API.
    Incluye tanto las categorías asociadas como las imágenes del producto.

    Atributos:
        child_category (ChildCategorySerializer): Campo de solo lectura que representa la subcategoría del producto.
        child_category_id (PrimaryKeyRelatedField): Campo de solo escritura que permite seleccionar una subcategoría mediante su ID.
        parent_category (ParentCategorySerializer): Campo de solo lectura que representa la categoría principal del producto.
        parent_category_id (PrimaryKeyRelatedField): Campo de solo escritura que permite seleccionar una categoría principal mediante su ID.
        images (ProductImageSerializer): Campo de solo lectura que devuelve las imágenes asociadas al producto.
    """

    child_category = ChildCategorySerializer(read_only=True, help_text="Subcategoría asociada al producto.")
    child_category_id = serializers.PrimaryKeyRelatedField(
        queryset=ChildCategory.objects.all(), source='child_category', write_only=True,
        help_text="ID de la subcategoría a la que pertenece el producto."
    )
    parent_category = ParentCategorySerializer(read_only=True, help_text="Categoría principal asociada al producto.")
    parent_category_id = serializers.PrimaryKeyRelatedField(
        queryset=ParentCategory.objects.all(), source='parent_category', write_only=True, required=False,
        help_text="ID de la categoría principal a la que pertenece el producto (opcional)."
    )
    images = ProductImageSerializer(many=True, read_only=True, help_text="Lista de imágenes asociadas al producto.")

    class Meta:
        model = Product
        fields = [
            'id', 'name_product', 'description', 'price', 'available_quantity', 'images', 
            'child_category', 'child_category_id', 'parent_category', 'parent_category_id', 
            'status', 'created_at', 'updated_at'
        ]
        extra_kwargs = {
            'name_product': {'help_text': 'Nombre del producto.'},
            'description': {'help_text': 'Descripción del producto.'},
            'price': {'help_text': 'Precio del producto.'},
            'available_quantity': {'help_text': 'Cantidad disponible del producto.'},
            'status': {'help_text': 'Estado del producto (Disponible, Agotado, Próximamente).'},
            'created_at': {'help_text': 'Fecha de creación del producto.'},
            'updated_at': {'help_text': 'Fecha de última actualización del producto.'},
        }
