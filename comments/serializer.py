from rest_framework import serializers
from .models import *
from asyncore import read

class Account_Img__Serializer(serializers.ModelSerializer):
    class Meta:
        model = Account_Img
        fields = '__all__'

class Account_Chats__Serializer(serializers.ModelSerializer):
    class Meta:
        model = Account_Chats
        fields = '__all__'

class Account_Contacts__Serializer(serializers.ModelSerializer):
    class Meta:
        model = Account_Contacts
        fields = '__all__'

class Account_Search_Chat__Serializer(serializers.ModelSerializer):
    class Meta:
        model = Account_Search_Chat
        fields = '__all__'

class Account__Serializer(serializers.ModelSerializer):
    account_img = Account_Img__Serializer(many=True, read_only=True)
    account_chats = Account_Chats__Serializer(many=True, read_only=True)
    account_contacts = Account_Contacts__Serializer(many=True, read_only=True)
    account_search_chat = Account_Search_Chat__Serializer(many=True, read_only=True)
    class Meta:
        model = Account
        fields = ["id" , "fname" , "tel_number" , "email" , "password" , "bio" , "link" , "age" , "online_time" , "img_end" , "tip" , "time" , "account_img" , "account_chats" , "account_contacts" , "account_search_chat"]

# chat

class Chat_Message__Serializer(serializers.ModelSerializer):
    class Meta:
        model = Chat_Message
        fields = "__all__"

class Chat_Member__Serializer(serializers.ModelSerializer):
    class Meta:
        model = Chat_Member
        fields = "__all__"

class Chat_Img__Serializer(serializers.ModelSerializer):
    class Meta:
        model = Chat_Img
        fields = "__all__"

class Chat__Serializer(serializers.ModelSerializer):
    chat_message = Chat_Message__Serializer(many=True, read_only=True)
    chat_chats = Chat_Member__Serializer(many=True, read_only=True)
    chat_img = Chat_Img__Serializer(many=True, read_only=True)
    class Meta:
        model = Chat
        fields = ["id" , "name" , "link" , "bio" , "id_create_user" , "id_called_user" , "img_end" , "tip" , "time" , "chat_message" , "chat_chats" , "chat_img"]






