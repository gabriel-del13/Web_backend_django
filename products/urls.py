from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'items', views.ProductViewSet)
router.register(r'category', views.CategoryViewSet)


urlpatterns = [

    path('products', include(router.urls)),


]