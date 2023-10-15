from .views import  EventsDetail , EventsList, EventCreateView
from django.urls import path

urlpatterns=[
    path('', EventsList.as_view(),name='event_list'),
    path('create/', EventCreateView.as_view(),name='event_create'),
    path('<int:pk>/',EventsDetail.as_view(), name = 'event_detail'),
    ]