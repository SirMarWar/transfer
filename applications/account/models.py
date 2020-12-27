from django.db import models
from django.contrib.auth.models import User


class Type(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    enable = models.BooleanField()


# Create your models here.
class State(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    enable = models.BooleanField()
    id_type = models.ForeignKey(Type, on_delete=models.CASCADE)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=50, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    img = models.ImageField(
        upload_to="profile", height_field=None, width_field=None, max_length=None
    )

    # state = models.ForeignKey("state", on_delete=models.CASCADE)

    def __str__(self):
        return self.name