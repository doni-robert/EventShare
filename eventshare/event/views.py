from django.shortcuts import render
from .models import Event, User

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_event= Event.objects.all().count()

    # Available books (status = 'a')

    # The 'all()' is implied by default.
    num_users = User.objects.count()

    context = {
        'num_event': num_event,
        'num_users': num_users,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)