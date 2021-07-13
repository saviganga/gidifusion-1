from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.expressions import F
from .managers import MyUserManager

# Create your models here.

class MyUser(AbstractUser):

    username = None
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_team = models.BooleanField(default=False)
    is_player = models.BooleanField(default=False)
    is_fan = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]


class Team(models.Model):
    
    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    coach = models.CharField(max_length=100,)
    phone = models.BigIntegerField(max_length=11, unique=True, null=False, blank=False)


class Player(models.Model):
    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')


class Fan(models.Model):

    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)

