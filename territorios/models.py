from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Territorio(models.Model):
    id_territorio = models.IntegerField(primary_key=True)
    nombre_territorio = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)  # Define un campo de tipo CharField para la categoría del territorio
    def _str_(self):
        return self.nombre_territorio
    
class Visita(models.Model): 
    id_visita = models.IntegerField(primary_key=True)
    nombre_capitan = models.CharField(max_length=50)  # Define un campo de tipo CharField para el nombre del capitán de la visita
    territorio = models.ForeignKey(Territorio, on_delete=models.CASCADE)  # Define un campo de tipo ForeignKey para relacionar con el modelo Territorio
    fecha_visita = models.DateField() 
    fecha_registro = models.DateField()  
    estado_visita = models.BooleanField(default=False)  
    # Define un campo de tipo BooleanField para el estado de la visita (terminado o no terminado), con un valor predeterminado de no terminado
    