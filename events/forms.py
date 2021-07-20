from django.db.models import fields
from django.forms import ModelForm
from django import forms
from django.db import transaction
from django.forms.models import model_to_dict

from events.models import Event, Tickets
from account.models import MyUser

class CreateEventForm(ModelForm):

    name = forms.CharField(max_length=100, required=True)
    date = forms.DateTimeField(required=True)
    # price = forms.DecimalField(max_digits=6, decimal_places=2, required=True)

    class Meta():
        
        model = Event
        fields = ['name', 'date',]

    @transaction.atomic
    def save(self):
        # vendor = MyUser
        name = self.cleaned_data.get('name')
        date = self.cleaned_data.get('date')
        # price = self.cleaned_data.get('price')
        event = Event.objects.create(name=name, date=date)
        return event

class CreateTicketForm(ModelForm):

    class Meta():

        model = Tickets
        fields = ['event', 'type', 'price']


