from django.urls import path, include
import account.views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', account.views.signup_view, name='signup'),
    path('accounts/signup/team/', account.views.team_signup_view, name='team-signup'),
    path('accounts/signup/player/', account.views.player_signup_view, name='player-signup'),
    path('accounts/signup/fan/', account.views.fan_signup_view, name='fan-signup'),
    path('accounts/signup/vendor', account.views.vendor_signup_view, name='vendor-signup'),
    path('payment/team/', account.views.team_payment_view, name='team-payment'),
]
