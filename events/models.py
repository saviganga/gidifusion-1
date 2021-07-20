from account.views import fan_signup_view
from django.db import models

from account.models import Vendor

# Create your models here.
class Event(models.Model):

    # vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateTimeField()
    # price

    def __str__(self) -> str:
        return f'{self.name} || {self.date}'


class Tickets(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    type = models.CharField(max_length=20, blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)

    @property
    def price_display(self):
        return f'NGN{self.price}'

    def __str__(self) -> str:
        return f'{self.event} || {self.type} || {self.price}'


