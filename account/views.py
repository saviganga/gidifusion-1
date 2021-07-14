from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_safe
from django.contrib.auth import authenticate, login, logout

from . import forms
from .models import MyUser as user

# Create your views here.

@require_safe
def signup_view(request):

    template = 'account/signup.html'
    return render(request, template)


@require_http_methods(['GET', 'POST'])
def team_signup_view(request):

    # confirm user authentication
    if request.user.is_authenticated:
        return redirect('signup')   # redirect to index/homepage

    # define formand template variables
    form = forms.TeamSignUpForm(request.POST or None)
    template = 'account/team_signup.html'
    template_vars = {'form': form}

    # validate form and save user
    if form.is_valid():
        new_team = form.save()
        new_team.save()
        return redirect('signup')

    return render(request, template, template_vars)



@require_http_methods(['GET', 'POST'])
def player_signup_view(request):

    if request.user.is_authenticated:
        return redirect('signup')

    form = forms.PlayerSignUpForm(request.POST or None)
    template = 'account/player_signup.html'
    template_vars = {'form': form}

    if form.is_valid():
        new_player = form.save()
        new_player.save()
        return redirect('signup')

    return render(request, template, template_vars)



@require_http_methods(['GET', 'POST'])
def fan_signup_view(request):

    if request.user.is_authenticated:
        return redirect('signup')

    form = forms.FanSignUpForm(request.POST or None)
    template = 'account/fan_signup.html'
    template_vars = {'form':form}

    if form.is_valid():
        new_fan = form.save()
        new_fan.save()
        return redirect('signup')

    return render(request, template, template_vars)