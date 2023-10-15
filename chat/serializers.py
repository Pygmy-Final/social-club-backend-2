from rest_framework import serializers
# from rest_framework.relations import PrimaryKeyRelatedField
from .models import Message
from accounts.models import CustomUser

class SenderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields=('id','username','first_name','last_name','email','gender','phonenumber','profilePicture','interests')

class MessagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

    def create(self, validated_data): #post
        user_id =self.context['request'].user.id
        validated_data['sender'].id=user_id
        return Message.objects.create(**validated_data) 

class MessageGetSerializer(serializers.ModelSerializer):
    sender = SenderInfoSerializer(read_only=True)
    receiver = SenderInfoSerializer(read_only=True)

    class Meta:
        model = Message
        fields = "__all__"

    def create(self, validated_data): #post
        user_id =self.context['request'].user.id
        validated_data['sender'].id=user_id
        return Message.objects.create(**validated_data) 



