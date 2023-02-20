from django.contrib import admin
from .models import *
# Register your models here.

# akk
admin.site.register(Account)
admin.site.register(Account_Img)
admin.site.register(Account_Chats)
admin.site.register(Account_Contacts)
admin.site.register(Account_Search_Chat)
# chat
admin.site.register(Chat)
admin.site.register(Chat_Img)
admin.site.register(Chat_Member)
admin.site.register(Chat_Message)