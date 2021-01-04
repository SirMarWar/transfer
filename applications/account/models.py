from django.db import models
from django.contrib.auth.models import User, Group
from ..shared.models import State, Type

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth = models.DateField(auto_now=False, auto_now_add=False)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    img = models.ImageField(upload_to="profile", null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    timezone = models.CharField(max_length=50, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name