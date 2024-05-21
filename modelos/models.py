from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Usuario(models.Model):
    nombre= models.CharField(max_length=45, verbose_name="Nombre")
    apellido= models.CharField(max_length=45, verbose_name="Apellido")
    telefono= models.CharField(max_length=10, verbose_name="Teléfono")
    fecha_nacimiento= models.DateField("Fecha Nacimiento")
    class TipoDocumento(models.TextChoices):
        CEDULA="CC",_("Cédula")
        TARJETA="TI",_("Tarjeta de Identidad")
        PASAPORTE="PP",_("Pasaporte")
    tipo_documento=models.CharField(max_length=2, choices=TipoDocumento.choices, verbose_name="Tipo de Documento")
    documento=models.PositiveIntegerField(verbose_name="Documento",unique=True)
    def _str_(self):
        return self.nombre+" "+self.apellido
    
