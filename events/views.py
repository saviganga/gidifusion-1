from events.models import Event, Tickets
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_safe
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required

from account.models import MyUser as user, Vendor
from events.forms import CreateEventForm, CreateTicketForm
# reverse

# Create your views here.

def list_events(request):

    events = Event.objects.all()
    template = 'events/list_events.html'
    template_vars = {'events': events}

    return render(request, template, template_vars)

@require_http_methods(['GET', 'POST'])
@permission_required(('admin.can_add_log_entry'))
def create_event_view(request):

    if not request.user.is_authenticated:
        # redirect/reverse to signup page
        return redirect('account:signup')

    # define form and template
    form = CreateEventForm(request.POST or None)
    #vendor = Vendor.objects.get(pk=request.user.pk)
    template = 'events/create_event.html'
    template_vars = {'form': form}

    # validate form and save
    if form.is_valid():
        new_event = form.save()
        # new_event.vendor = vendor
        new_event.save()

        # redirect to events page
        return redirect('create-ticket')
    
    return render(request, template, template_vars)


@require_http_methods(['GET', 'POST'])
@permission_required(('admin.can_add_log_entry'))
def create_ticket_view(request):

    form = CreateTicketForm(request.POST or None)
    template = 'events/create_ticket.html'
    template_vars = {'form': form}

    if form.is_valid():

        new_ticket = form.save(commit=False)
        new_ticket.save()

        return redirect('list-tickets')

    return render(request, template, template_vars)


def list_tickets_view(request):

    tickets = Tickets.objects.all()
    template = 'events/list_tickets.html'
    template_vars = {'tickets': tickets}

    return render(request, template, template_vars)



def list_team_tickets(request):

    
    if not request.session['team']:
        return redirect('events')

    team_tickets = Tickets.objects.filter(type='Team')
    template = 'events/list_team_tickets.html'
    template_vars = {'team_tickets': team_tickets}

    return render(request, template, template_vars)




def list_fan_ticket_view(request):

    if not request.session['fan']:
        return redirect('events')

    fan_tickets = Tickets.objects.filter(type='Fan')
    template = 'events/list_fan_tickets.html'
    template_vars = {'fan_tickets': fan_tickets}

    return render(request, template, template_vars)



def display_team_ticket_view(request, ticket_id):

    if not request.session['team']:
        return redirect('events')
    

    team_ticket = Tickets.objects.get(pk=ticket_id, type='Team')
    template = 'events/display_team_ticket.html'
    template_vars = {'team_ticket': team_ticket}

    return render(request, template, template_vars)


def display_fan_ticket_view(request, ticket_id):


    if not request.session['fan']:
        return redirect('events')

    fan_ticket = Tickets.objects.get(pk=ticket_id, type='Fan')
    template = 'events/display_fan_ticket.html'
    template_vars = {'fan_ticket': fan_ticket}

    return render(request, template, template_vars)
