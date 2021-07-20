from events.models import Event
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_safe
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required

from account.models import MyUser as user, Vendor
from events.forms import CreateEventForm
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
        return redirect('events')
    
    return render(request, template, template_vars)
