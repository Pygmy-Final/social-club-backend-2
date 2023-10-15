from .models import CustomUser, Follow
from .serializers import FollowListSerializer, UserProfileSerializer, FollowCreateAndDetailsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import UserWritePermiss
from rest_framework.filters import SearchFilter
from django.db.models import Q

class UserProfileListView(generics.ListAPIView):
    """
    user list and can filter by interests
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends= [SearchFilter]
    search_fields = ['interests']


class UserProfileCreateView(generics.CreateAPIView):
    """
    create user view and allow any user
    """
    queryset = CustomUser.objects.all() 
    serializer_class = UserProfileSerializer
    permission_classes = (AllowAny,)
  
class UserInfoView(generics.ListAPIView, UserWritePermiss):
    """
    user detail info by searching by username
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (UserWritePermiss,)
    filter_backends= [SearchFilter]
    search_fields = ['username']

class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView, UserWritePermiss):
    """
    user detail info by id
    """
    queryset = CustomUser.objects.all() 
    serializer_class = UserProfileSerializer
    permission_classes = (UserWritePermiss,)


class FollowListView(generics.ListAPIView):
    """
    follow list view by filtering by from_user = regetered one
    """
    serializer_class = FollowListSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends= [SearchFilter]
    search_fields = ['from_user']

    def  get_queryset(self, *args, **kwargs):
        user_id = str(self.request.user) 
        queryset = Follow.objects.filter(from_user = user_id)
        return queryset

class FollowCreateView(generics.CreateAPIView):
    """
    create/add follow
    """
    queryset = Follow.objects.all()
    serializer_class = FollowCreateAndDetailsSerializer
    permission_classes = (IsAuthenticated,)