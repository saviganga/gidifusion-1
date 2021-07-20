from django.urls import path, include
import events.views

urlpatterns = [
    path('', events.views.list_events, name='events'),
    path('create-event/', events.views.create_event_view, name='create-event'),
    path('create-ticket/', events.views.create_ticket_view, name='create-ticket'),
    path('list-tickets/', events.views.list_tickets_view, name='list-tickets'),    
    path('list-team-tickets/', events.views.list_team_tickets, name='list-team-tickets'),
]