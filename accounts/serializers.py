from .models import CustomUser, Follow
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework import fields

interests_list = [('Reading', 'Reading'),
             ('Cycling', 'Cycling'),
             ('Hiking', 'Hiking'),
             ('Drawing', 'Drawing'),
             ('Photography', 'Photography'),
             ('Swimming', 'Swimming'),
             ('Sleeping', 'Sleeping'),
             ('Sports', 'Sports'),
             ('Gaming', 'Gaming')]

class CustomMultipleChoiceField(fields.MultipleChoiceField, serializers.HyperlinkedModelSerializer):
    def to_representation(self, value):
        returnval = list(super().to_representation(value))
        return returnval

class UserProfileSerializer(serializers.ModelSerializer):
    interests = fields.MultipleChoiceField(choices=interests_list)
    class Meta:
        model = CustomUser
        fields = ('id','username','first_name','last_name','email','password','gender','phonenumber','profilePicture','interests')
    
    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

class UserSerializer(serializers.ModelSerializer):
    interests = fields.MultipleChoiceField(choices=interests_list)
    class Meta:
        model = CustomUser
        fields = ('id','username','first_name','last_name','email','gender','phonenumber','profilePicture','interests')
    
    
    
class FollowListSerializer(serializers.ModelSerializer):
    to_user = UserSerializer(read_only=True)
    from_user = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = "__all__"

    def create(self, validated_data): #post
        user_id =self.context['request'].user.id
        validated_data['from_user'].id=user_id
        return Follow.objects.create(**validated_data)  


class FollowCreateAndDetailsSerializer(serializers.ModelSerializer):

    def create(self, validated_data): #post
        user_id =self.context['request'].user.id
        validated_data['from_user'].id=user_id
        return Follow.objects.create(**validated_data)  
        
    class Meta:
        model = Follow
        fields = "__all__"




