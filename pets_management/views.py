from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Pet
from .serializers import PetSerializer

# --- Vista para la Página de Bienvenida (Dashboard) ---
def home_view(request):
    return render(request, 'pets_management/home.html')

# --- Tu ViewSet existente de Mascotas ---
class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all().order_by('-created_at')
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        total_pets = self.queryset.count()
        available_pets = self.queryset.filter(status='available').count()
        
        data = {
            "mensaje": "Estadísticas obtenidas con éxito",
            "total_mascotas": total_pets,
            "disponibles": available_pets
        }
        return Response(data, status=status.HTTP_200_OK)

