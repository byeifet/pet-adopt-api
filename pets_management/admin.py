from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    # 1. Columnas que se mostrarán en la tabla principal del admin
    list_display = ('id', 'name', 'species', 'breed', 'age_months', 'status', 'created_at')
    
    # 2. Filtros laterales para buscar rápidamente por categorías
    list_filter = ('species', 'status', 'created_at')
    
    # 3. Barra de búsqueda superior para encontrar registros por nombre o raza
    search_fields = ('name', 'breed', 'description')
    
    # 4. Campos que se pueden editar directamente desde la lista sin entrar al detalle
    list_editable = ('status',)
    
    # 5. Orden por defecto (las mascotas más nuevas primero)
    ordering = ('-created_at',)