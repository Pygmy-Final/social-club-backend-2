from rest_framework import serializers
from .models import Event
from accounts.models import CustomUser

class SenderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields=('id','username','first_name','last_name','email','gender','phonenumber','profilePicture','interests')

class EventCreateAndDeleteSerialzer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Event

    def create(self, validated_data): #post
        user_id =self.context['request'].user.id
        validated_data['EventCreator'].id=user_id
        return Event.objects.create(**validated_data)

class EventListSerialzer(serializers.ModelSerializer):
    EventCreator = SenderInfoSerializer(read_only=True)

    class Meta:
        model = Event
        fields = "__all__"

    def create(self, validated_data): #post
        user_id =self.context['request'].user.id
        validated_data['EventCreator'].id=user_id
        return Event.objects.create(**validated_data)

    

