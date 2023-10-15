from django.db import models
from django.db.models.fields import IntegerField
from django_mysql.models import ListTextField
from multiselectfield import MultiSelectField
from django.conf import settings

class Event(models.Model):
    EventName        = models.CharField(max_length=256)
    EventDescription = models.CharField(max_length=256)
    EventLocation    = models.CharField(max_length=256)
    EventCategory    = MultiSelectField(max_length=26, choices=[  ('Reading', 'Reading'), ('Cycling', 'Cycling'),
                                                                  ('Hiking','Hiking'), ('Drawing', 'Drawing'),('Photography', 'Photography'),
                                                                  ('Swimming','Swimming'),('Sleeping','Sleeping'),('Sports','Sports'),('Gaming','Gaming')])
    EventStartTime  = models.DateTimeField(null=True)
    EventCreator    = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
    EventParticipants = ListTextField(  base_field=IntegerField(),
                                        size=50,  null=True , default=0) 


