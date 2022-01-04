from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup

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
        return render(request,'meetups/meetup-details.html',{
            'meetup_found':True,
            'meetup_title':seleted_meetup.title,
            'meetup_description':seleted_meetup.description
        })
    except Exception as e:
         return render(request,'meetups/meetup-details.html',{
            'meetup_found':False
        })
