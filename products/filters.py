from django_filters import rest_framework as filters
from .models import Product, ChildCategory

class ProductFilter(filters.FilterSet):
    parent_category = filters.NumberFilter(field_name='child_category__parent_category')

    class Meta:
        model = Product
        fields = ['status', 'child_category', 'parent_category']


class ChildCategoryFilter(filters.FilterSet):
    child_category_id = filters.NumberFilter(field_name='child_category__id', lookup_expr='exact')
    child_category_name = filters.CharFilter(field_name='chikd_category__name', lookup_expr='icontains')
    parent_category_id = filters.NumberFilter(field_name='parent_category__id', lookup_expr='exact')
    parent_category_name = filters.CharFilter(field_name='parent_category__name', lookup_expr='icontains')

    class Meta:
        model = ChildCategory
        fields = ['child_category_id', 'child_category_name', 'parent_category_id', 'parent_category_name']