from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    meetups = [
            {   
                'title':'the first meetups',
                'location':'colombo',
                'slug':'first-meetup'
            },
            {
                'title':'second meetup',
                'location':'galle',
                'slug':'second-meetup'
            }
                ]
    return render(request,'meetups/index.html',{
        'show_meetups':True,
        'meetups':meetups
    })
