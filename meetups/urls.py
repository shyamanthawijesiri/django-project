from django.urls import path
from . import views
urlpatterns =[
    path('meetups/',views.index, name='all-meetups'),
    path('meetups/<slug:meetup_slug>/',views.meeup_details, name='meetup-detail')
    
    ]