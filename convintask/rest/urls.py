from django.urls import path

from . import views

urlpatterns = [
    path('v1/calendar/init', views.UserViews.as_view(), name='auth'),
    path('v1/calendar/redirect', views.EventsView.as_view(), name='redirect'),
]