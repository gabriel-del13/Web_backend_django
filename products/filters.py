from django_filters import rest_framework as filters
from .models import Product, ChildCategory, ParentCategory

class ProductFilter(filters.FilterSet):
    # Permite filtrar por múltiples parent_category
    parent_category = filters.ModelMultipleChoiceFilter(
        field_name='child_category__parent_category',
        queryset=ParentCategory.objects.all()
    )
    
    # Permite filtrar por múltiples child_category
    child_category = filters.ModelMultipleChoiceFilter(
        field_name='child_category',
        queryset=ChildCategory.objects.all()
    )
    class Meta:
        model = Product
        fields = ['status', 'child_category', 'parent_category']


# Filtro personalizado para ChildCategory en Django
class ChildCategoryFilter(filters.FilterSet):
    
    # Filtra por el ID de la subcategoría, utilizando una coincidencia exacta
    child_category_id = filters.NumberFilter(field_name='child_category__id', lookup_expr='exact')
    
    # Filtra por el nombre de la subcategoría, utilizando una búsqueda no sensible a mayúsculas/minúsculas
    child_category_name = filters.CharFilter(field_name='chikd_category__name', lookup_expr='icontains')
    
    # Filtra por el ID de la categoría padre, utilizando una coincidencia exacta
    parent_category_id = filters.NumberFilter(field_name='parent_category__id', lookup_expr='exact')
    
    # Filtra por el nombre de la categoría padre, utilizando una búsqueda no sensible a mayúsculas/minúsculas
    parent_category_name = filters.CharFilter(field_name='parent_category__name', lookup_expr='icontains')

    class Meta:
        model = ChildCategory
        # Define los campos que se pueden filtrar usando el filtro personalizado
        fields = ['child_category_id', 'child_category_name', 'parent_category_id', 'parent_category_name']