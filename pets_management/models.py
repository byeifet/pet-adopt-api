# pets_management/models.py

from django.db import models

class Pet(models.Model):
    STATUS_CHOICES = [
        ('available', 'Disponible'),
        ('pending', 'Pendiente de adopción'),
        ('adopted', 'Adoptado'),
    ]
    
    SPECIES_CHOICES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Otro', 'Otro'),
    ]

    name = models.CharField(max_length=100, verbose_name="Nombre")
    species = models.CharField(max_length=50, choices=SPECIES_CHOICES, verbose_name="Especie")
    breed = models.CharField(max_length=100, blank=True, null=True, verbose_name="Raza")
    
    # Nuevos campos de edad separados
    age_years = models.PositiveIntegerField(default=0, verbose_name="Edad (Años)")
    age_months = models.PositiveIntegerField(default=0, verbose_name="Edad (Meses)")
    
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="Estado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.species}) - {self.age_years} año(s) y {self.age_months} mes(es)"