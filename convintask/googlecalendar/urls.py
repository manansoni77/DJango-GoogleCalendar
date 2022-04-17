from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('tapi', views.test_api, name='tapi'),
    path('api', views.UserViews.as_view()),
    path('api/redirect',views.EventsView.as_view(), name='redirect'),
]