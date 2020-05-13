from django.db import models
import uuid

# Create your models here.
class Luminosity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Tipo = models.CharField(verbose_name='Tipo', max_length=20)
    Valor = models.IntegerField(verbose_name='Valor')
    latitud = models.IntegerField(verbose_name='latitud')
    longitud = models.IntegerField(verbose_name='longitud')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    