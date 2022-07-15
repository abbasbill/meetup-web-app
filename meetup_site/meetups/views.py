
from django.shortcuts import render, redirect

from meetups.forms import RegistrationForm
# Create your views here.
from .models import meetup, Participant
from .forms import RegistrationForm

def index(request):
    meetups= meetup.objects.all()
    return render(request, "meetups/index.html",{
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participants, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participant.add(participants)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

        return render(request, "meetups/meetup-details.html",{
                'meetup_found': True,
                'meetup':selected_meetup,
                'form': registration_form
            })        
    except Exception as exc:
        print(exc)
        return render(request, "meetups/meetup-details.html",{
            'meetup_found': False
        })    
 

def confirm_registration(request, meetup_slug):
    Meetup = meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'organizerEmail': Meetup.organizerEmail
    })         

