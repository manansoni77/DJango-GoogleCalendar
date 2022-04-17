from email.policy import HTTP
from django import views
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EventSerializer, UserSerializer
from .models import Event, User

from .calendar_API import test_calendar, get_token, get_events
# Create your views here.

def index(request):
    return HttpResponse('Hello World! At Google Index')

def test_api(request):
    get_token()
    context = {"events" : get_events()}
    return render(request,'list_events.html',context)

class UserViews(APIView):
    def post(self, request):
        data = request.POST
        print(data['user_name'])
        CREDS = None
        user = User.objects.filter(user_name=data['user_name']).first()
        if user:
            print('found user!')
        else:
            print('new user!')
            user = User.objects.create(user_name=data['user_name'])
        creds = get_token(user.user_token)
        user.user_token = creds.to_json()
        user.save()
        return redirect('api/redirect')

class EventsView(APIView):
    def get(self,request):
        events = get_events()
        return Response(events)