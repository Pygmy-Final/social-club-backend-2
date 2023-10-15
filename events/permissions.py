from rest_framework.permissions import BasePermission, SAFE_METHODS

class EventUserWritePermiss(BasePermission):
    message ='Editing Event is restrected to the user only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.EventCreator == request.user

