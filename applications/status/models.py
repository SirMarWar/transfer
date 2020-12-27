from django.db import models

class Type(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    enable = models.BooleanField()

# Create your models here.
class State(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    enable = models.BooleanField()
    id_state = models.ForeignKey(Type, on_delete=models.CASCADE)