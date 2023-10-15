import django_filters
from .models import CustomUser

class UserFilter(django_filters.FilterSet):
    class Meta():
        model = CustomUser
        fields = ('first_name','interests')
