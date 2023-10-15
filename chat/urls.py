from django.urls import path
from .views import MessageView, MessageDetailView, MessageGetView


urlpatterns = [
    path("create/", MessageView.as_view(), name="message_craete"),
    path("<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("", MessageGetView.as_view(), name = 'message_list'),

]

