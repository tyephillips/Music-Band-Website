from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event


# Create your views here.
def home(request):
    """
    Handles the request to display the homepage of the website.
    """
    return render(request, 'horizons/home.html')


def events(request):
    """
    Handles the request to  display the list of upcoming events. 
    """
    # Retrieves all events from the database.
    events = Event.objects.all()
    return render(request, 'horizons/events.html', {'events': events})


@login_required
def member_area(request):
    """
    Handles the request to display the member-only area. This view will
    only be accessible to authenticated users.
    """
    return render(request, 'horizons/member_area.html')


def register(request):
    """
    Handles user registration by providing a form to create a new
    account.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user to the database.
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!"
                             "You can now login.")
            # Redirect to login page.
            return redirect('horizons:login')
    else:
        form = UserCreationForm()
    return render(request, 'horizons/register.html', {'form': form})


@login_required
def profile(request):
    """
    Displays the user's profile page. Only accessible to authenticated
    users.
    """
    return render(request, 'horizons/profile.html')
