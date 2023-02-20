from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class Account__ViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = Account__Serializer

class Account_Img__ViewSet(ModelViewSet):
    queryset = Account_Img.objects.all()
    serializer_class = Account_Img__Serializer

class Account_Chats__ViewSet(ModelViewSet):
    queryset = Account_Chats.objects.all()
    serializer_class = Account_Chats__Serializer

class Account_Contacts__ViewSet(ModelViewSet):
    queryset = Account_Contacts.objects.all()
    serializer_class = Account_Contacts__Serializer

class Account_Search_Chat__ViewSet(ModelViewSet):
    queryset = Account_Search_Chat.objects.all()
    serializer_class = Account_Search_Chat__Serializer

# chat

class Chat_Message__ViewSet(ModelViewSet):
    queryset = Chat_Message.objects.all()
    serializer_class = Chat_Message__Serializer

class Chat_Member__ViewSet(ModelViewSet):
    queryset = Chat_Member.objects.all()
    serializer_class = Chat_Member__Serializer

class Chat_Img__ViewSet(ModelViewSet):
    queryset = Chat_Img.objects.all()
    serializer_class = Chat_Img__Serializer

class Chat__ViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = Chat__Serializer




