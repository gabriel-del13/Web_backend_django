
from rest_framework import viewsets, status, filters, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser

from django.http import Http404
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, ProductImage, ChildCategory, ParentCategory
from .serializers import ProductSerializer, ChildCategorySerializer, ParentCategorySerializer
from favorites.models import Favorites 
from .filters import ProductFilter, ChildCategoryFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['name_product', 'updated_at', 'price', 'available_quantity']

    def get_queryset(self):
        queryset = Product.objects.all()
        search_term = self.request.query_params.get('search', None)
        ordering = self.request.query_params.get('ordering', '-updated_at')

        filters = Q()
        
        if search_term:
            filters &= Q(name_product__icontains=search_term)
        
        queryset = queryset.filter(filters)
        
        return queryset.order_by(ordering)
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        product = serializer.save()
        images_data = self.request.FILES.getlist('images')
        for image_data in images_data:
            ProductImage.objects.create(product=product, image=image_data)

    def perform_update(self, serializer):
        product = serializer.save()
        images_data = self.request.FILES.getlist('images')
        for image_data in images_data:
            ProductImage.objects.create(product=product, image=image_data)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response(
                {"error": "Producto no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def add_to_favorites(self, request, pk=None):
        product = self.get_object()
        favorite, created = Favorites.objects.get_or_create(user=request.user, product=product)
        if created:
            return Response({'status': 'product added to favorites'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'product already in favorites'}, status=status.HTTP_200_OK)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class ChildCategoryViewSet(viewsets.ModelViewSet):
    queryset = ChildCategory.objects.all()
    serializer_class = ChildCategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ChildCategoryFilter
    # Permite ordenar los resultados por el nombre de la categoría o la fecha de última actualización
    ordering_fields = ['name_childcategory', 'updated_at']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


class ParentCategoryViewSet(viewsets.ModelViewSet):
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = ['name_parentcategory', 'updated_at']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    
    