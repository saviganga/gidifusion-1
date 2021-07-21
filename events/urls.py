from django.urls import path, include
import events.views

urlpatterns = [
    path('', events.views.list_events, name='events'),
    path('create-event/', events.views.create_event_view, name='create-event'),
    path('create-ticket/', events.views.create_ticket_view, name='create-ticket'),
    path('list-tickets/', events.views.list_tickets_view, name='list-tickets'),    
    path('list-team-tickets/', events.views.list_team_tickets, name='list-team-tickets'),
    path('team-ticket/<int:ticket_id>/', events.views.display_team_ticket_view, name='display-team-ticket'),
    path('list-fan-tickets/', events.views.list_fan_ticket_view, name='list-fan-tickets'),
    path('fan-ticket/<int:ticket_id>/', events.views.display_fan_ticket_view, name='display-fan-ticket'),
]