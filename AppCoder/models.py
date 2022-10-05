from django.db import models
from unittest.util import _MAX_LENGTH

class Familiar(models.Model):
    Nombre=models.CharField(max_length=50)
    Edad=models.IntegerField()
    Nacimiento=models.DateField()
