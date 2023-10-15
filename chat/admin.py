from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ['message', 'seen','sender', 'receiver', 'date_created']
    model = Message
    
    def save_model(self, request, obj, form, change):
        if obj.receiver != request.user:
            obj.sender = request.user
            obj.save()
            
admin.site.register(Message)