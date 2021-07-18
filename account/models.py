from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.expressions import F
#from phonenumber_field.modelfields import PhoneNumberField
from .managers import MyUserManager

# Create your models here.

class MyUser(AbstractUser):

    username = None
    #name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_team = models.BooleanField(default=False)
    is_player = models.BooleanField(default=False)
    is_fan = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'{self.email} '


class Team(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    coach = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=11, unique=True, null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.name}'

class Player(models.Model):
    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    position = models.CharField(max_length=50, blank=False, null=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self) -> str:
        return f'{self.first_name} | {self.position}' 

class Fan(models.Model):

    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}: {self.profile.email}'

class Vendor(models.Model):

    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)