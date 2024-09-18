from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    parent_category = filters.NumberFilter(field_name='category__parent_category')

    class Meta:
        model = Product
        fields = ['status', 'category', 'parent_category']
