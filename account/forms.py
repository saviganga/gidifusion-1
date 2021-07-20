from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from django.contrib.auth import get_user_model
from account.models import Team, Player, Fan, Vendor

class TeamSignUpForm(UserCreationForm):

    # add extra fields not in the user model
    name = forms.CharField(max_length=100, required=True)
    coach = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=11, required=True)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['email', 'name', 'coach', 'phone']

    @transaction.atomic # enforces single database operation
    def save(self):
        user = super().save(commit=False)
        user.is_team = True
        user.save()
        name = self.cleaned_data.get('name')
        coach = self.cleaned_data.get('coach')
        phone = self.cleaned_data.get('phone')
        team = Team.objects.create(profile=user, name=name, coach=coach, phone=phone)
        return user



class PlayerSignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    position = forms.CharField(max_length=50, required=True)
    team = forms.ModelChoiceField(queryset=Team.objects.all())

    class Meta(UserCreationForm.Meta):

        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'position', 'team']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_player = True
        user.save()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        team = self.cleaned_data.get('team')
        player = Player.objects.create(profile=user, first_name=first_name, last_name=last_name, team=team)
        return user


class FanSignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    class Meta(UserCreationForm.Meta):

        model = get_user_model()
        fields = ['email', 'first_name', 'last_name',]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_fan = True
        user.save()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        fan = Fan.objects.create(profile=user, first_name=first_name, last_name=last_name)
        return user


class VendorSignUpForm(UserCreationForm):

    name = forms.CharField(max_length=50, required=True)

    class Meta(UserCreationForm.Meta):
        
        model = get_user_model()
        fields = ['email', 'name']

        @transaction.atomic
        def save(self):
            user = super().save(commit=False)
            user.is_vendor = True
            user.save()
            name = self.cleaned_data.get('name')
            vendor = Vendor.objects.create(profile=user, name=name)
            return user



