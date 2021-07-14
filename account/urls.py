from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('accounts/signup/team/', views.team_signup_view, name='team-signup'),
    path('accounts/signup/player/', views.player_signup_view, name='player-signup'),
    #path('accounts/signup/fan/', views.fan_signup_view, name='fan-signup'),
]
