from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'items', views.ProductViewSet)
router.register(r'child_category', views.ChildCategoryViewSet)
router.register(r'parent_category', views.ParentCategoryViewSet)



urlpatterns = [

    path('', include(router.urls)),


]