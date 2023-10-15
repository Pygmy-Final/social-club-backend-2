from django.shortcuts import render
from .models import Event
from .serializers import EventCreateAndDeleteSerialzer,EventListSerialzer
from rest_framework import generics
from .permissions import EventUserWritePermiss
from rest_framework.permissions import IsAuthenticated

class EventsList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerialzer
    permission_classes = (IsAuthenticated,)

class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateAndDeleteSerialzer
    permission_classes = (IsAuthenticated,)

class EventsDetail(generics.RetrieveUpdateDestroyAPIView,EventUserWritePermiss):
    queryset = Event.objects.all()
    serializer_class = EventCreateAndDeleteSerialzer
    permission_classes = (EventUserWritePermiss,)

