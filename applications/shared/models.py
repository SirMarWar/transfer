from django.db import models

# Create your models here.


class Type(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    enable = models.BooleanField()

    def __str__(self):
        return self.code + " :: " + self.name


# Create your models here.
class State(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    display = models.CharField(max_length=50, null=True)
    color = models.CharField(max_length=50, null=True)
    icon = models.CharField(max_length=50, null=True)
    enable = models.BooleanField()
    id_type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.code + " :: " + self.name


class Country(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    id_api = models.CharField(max_length=50)

    def __str__(self):
        return self.name
