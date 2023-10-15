from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Follow


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']
    fieldsets =  UserAdmin.fieldsets + (
        ("Extra information", {"fields": ("phonenumber",'gender','profilePicture','interests', 'user'),},
        
        ),
    )

class FollowAdmin(admin.ModelAdmin):
    list_display = ['to_user', 'from_user',]
    model = Follow
    
    def save_model(self, request, obj, form, change):
        """
        will save user who logged in in from_user column in db
        """
        if obj.to_user != request.user:
            obj.from_user = request.user
            obj.save()

# filter duplicate relationships in frontend, by looping through all objects.

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Follow, FollowAdmin)
