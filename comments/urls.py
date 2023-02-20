from .views import * 
from django.urls import path , include
from rest_framework import routers
# akk
router = routers.DefaultRouter()
router.register('account', Account__ViewSet)
router.register('account_img', Account_Img__ViewSet)
router.register('account_chats', Account_Chats__ViewSet)
router.register('account_contacts', Account_Contacts__ViewSet)
router.register('account_search_chat', Account_Search_Chat__ViewSet)

# chat

router.register('chat', Chat__ViewSet)
router.register('chat_img', Chat_Img__ViewSet)
router.register('chat_member', Chat_Member__ViewSet)
router.register('chat_message', Chat_Message__ViewSet)


urlpatterns = [
    path('',include(router.urls)),
]