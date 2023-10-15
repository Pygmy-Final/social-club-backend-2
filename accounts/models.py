from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField
from django.conf import settings

class CustomUser(AbstractUser):
    # user for chat id for current
    gender        = models.CharField(max_length=26,choices=[('Male', 'Male'), ('Female', 'Female')],default='Male')
    phonenumber   = models.IntegerField(null=True)
    profilePicture= models.URLField(max_length=1000,default='https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128')
    interests     = MultiSelectField(max_length=100,null=True, choices=[  
                                                ('Reading', 'Reading'),
                                                ('Cycling', 'Cycling'),
                                                ('Hiking','Hiking'),
                                                ('Drawing', 'Drawing'),
                                                ('Photography', 'Photography'),
                                                ('Swimming','Swimming'),
                                                ('Sleeping','Sleeping'),
                                                ('Sports','Sports'),
                                                ('Gaming','Gaming')])

    def __str__(self):
        return str(self.id)


class Follow(models.Model):

	to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
	from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)
    
	def __str__(self):
		return str(self.id)

