from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Service, ServiceImage
from .serializers import ServiceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        service = serializer.save()
        images_data = self.request.FILES.getlist('images')
        for image_data in images_data:
            ServiceImage.objects.create(service=service, image=image_data)

    def perform_update(self, serializer):
        service = serializer.save()
        images_data = self.request.FILES.getlist('images')
        for image_data in images_data:
            ServiceImage.objects.create(service=service, image=image_data)