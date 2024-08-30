from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Favorites
from .serializers import FavoritesSerializer

class FavoritesViewSet(viewsets.ModelViewSet):
    serializer_class = FavoritesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorites.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def remove_from_favorites(self, request, pk=None):
        favorites = self.get_object()
        favorites.delete()
        return Response({'status': 'product removed from favorites'}, status=status.HTTP_200_OK)