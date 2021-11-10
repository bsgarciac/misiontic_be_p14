from django.db import models

# Create your models here.

class Soporte(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)	
    age = models.IntegerField(null=True, blank=True)	
    is_active = models.BooleanField(default=True)


class PQR(models.Model):
    id = models.AutoField(primary_key=True)
    soporte = models.ForeignKey(Soporte, on_delete=models.SET_NULL, null=True)
    tipo = models.CharField(max_length=32)
    info = models.TextField()	
    created = models.DateField()
