from django.db import models

class Usuario(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
# Create your models here.
