from django.shortcuts import redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User

from .calendar_API import get_token, get_events
# Create your views here.

class UserViews(APIView):
    def post(self, request):
        data = request.POST
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
        return redirect('redirect')

class EventsView(APIView):
    def get(self,request):
        print('EVENTS...')
        events = get_events()
        return Response(events[-1])