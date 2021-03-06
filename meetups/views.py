from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import RegistrationForm
from .models import Meetup, Participants

# Create your views here.
def index(request):
    # meetups = [
    #         {   
    #             'title':'the first meetups',
    #             'location':'colombo',
    #             'slug':'first-meetup'
    #         },
    #         {
    #             'title':'second meetup',
    #             'location':'galle',
    #             'slug':'second-meetup'
    #         }
    #             ]
    meetups = Meetup.objects.all()
    return render(request,'meetups/index.html',{
        # 'show_meetups':True,
        'meetups':meetups
    })

def meeup_details(request,meetup_slug):
    # seleted_meetup = {
    #                     'title':'first meetup',
    #                     'description':'this is the first meetups'
    #                 }
    # return render(request,'meetups/meetup-details.html',{
    #     'meetup_title':seleted_meetup['title'],
    #     'meetup_description':seleted_meetup['description']
    # })
    try:
        seleted_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registraion_form = RegistrationForm()
            
        else:
            registraion_form = RegistrationForm(request.POST)
            if registraion_form.is_valid():
                # participants = registraion_form.save()
                user_email = registraion_form.cleaned_data['email']
                participant,_=Participants.objects.get_or_create(email=user_email)
                seleted_meetup.Participants.add(participant)
                return redirect('confirm-registration')

        return render(request,'meetups/meetup-details.html',{
                'meetup_found':True,
                'meetup':seleted_meetup,
                'form': registraion_form
                # 'meetup_title':seleted_meetup.title,
                # 'meetup_description':seleted_meetup.description
            })     
    except Exception as e:
        print(e)
        return render(request,'meetups/meetup-details.html',{
        'meetup_found':False
        })

def confirm_registration(request):
    return render(request, 'meetups/registration-success.html')