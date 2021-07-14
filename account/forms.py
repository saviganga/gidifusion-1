from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from django.contrib.auth import get_user_model
from account.models import MyUser, Team, Player, Fan

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