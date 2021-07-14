from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from django.contrib.auth import get_user_model
from account.models import Team, Player, Fan

class TeamSignUpForm(UserCreationForm):

    # add extra fields not in the user model
    coach = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=11, required=True)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['name', 'email', 'coach', 'phone']

    @transaction.atomic # enforces single database operation
    def save(self):
        user = super().save(commit=False)
        user.is_team = True
        user.save()
        coach = self.cleaned_data.get('coach')
        phone = self.cleaned_data.get('phone')
        team = Team.objects.create(profile=user, coach=coach, phone=phone)
        return user



class PlayerSignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    team = forms.ModelChoiceField(queryset=Team.objects.all())

    class Meta(UserCreationForm.Meta):

        model = get_user_model()
        fields = ['first_name', 'last_name', 'name', 'email', 'team']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_player = True
        user.save()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        team = self.cleaned_data.get('team')
        player = Player.objects.create(profile=user, first_name=first_name, last_name=last_name, team=team)
        #player.team.add(*self.cleaned_data.get('team'))
        return user