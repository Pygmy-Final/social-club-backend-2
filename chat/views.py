from .serializers import MessageGetSerializer, MessagePostSerializer
from .models import  Message
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django.db.models import Q

class MessageView(generics.CreateAPIView):
    # queryset = Message.objects.all()
    serializer_class = MessagePostSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends= [SearchFilter]
    search_fields = ['from_user']

    def  get_queryset(self, *args, **kwargs):
        user_id = str(self.request.user) 
        queryset = Message.objects.filter(Q(sender = user_id) | Q(receiver=user_id))
        return queryset

class MessageGetView(generics.ListAPIView):
    serializer_class = MessageGetSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends= [SearchFilter]
    search_fields = ['from_user']

    def  get_queryset(self, *args, **kwargs):
        user_id = str(self.request.user) 
        # not_deleted = User.objects.filter(Q(active=True) & Q(is_deleted=False)
        queryset = Message.objects.filter(Q(sender = user_id) | Q(receiver=user_id))
        return queryset

class MessageDetailView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessagePostSerializer
    permission_classes = [IsAuthenticated,]

