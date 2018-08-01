from django.db import models

# Create your models here.
class Picture(models.Model):
    imagen=models.ImageField("Imagen",upload_to='images')
