from django.urls import path, include
import events.views

urlpatterns = [
    path('', events.views.list_events, name='events'),
    path('events/create', events.views.create_event_view, name='create-event'),
]