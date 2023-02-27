from django.db import models

# Create your models here.

# for accaunt info

class Account(models.Model):
    id = models.CharField(max_length=20 , primary_key=True)
    fname = models.CharField(max_length=40)
    tel_number = models.CharField(max_length=20 , null=True , blank=True)
    email = models.CharField(max_length=100 , null=True , blank=True)
    password = models.CharField(max_length=16)
    bio = models.CharField(max_length=200 , null=True , blank=True)
    link = models.CharField(max_length=30 , null=True , blank=True )
    age = models.CharField(max_length=3 , null=True , blank=True)
    online_time = models.CharField(max_length=20 , null=True , blank=True)
    img_end = models.CharField(max_length=200 , null=True , blank=True)
    tip = models.CharField(max_length=10)
    time = models.CharField(max_length=20)
    
    def __str__(self):
        return self.id

class Account_Img(models.Model):
    link = models.CharField(max_length=200)
    time = models.CharField(max_length=20)
    acc_id = models.ForeignKey('Account' , on_delete=models.CASCADE, related_name='account_img')
    
    def __str__(self):
        return self.link

class Account_Chats(models.Model):
    chat_id = models.CharField(max_length=20)
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=40)
    user_img = models.CharField(max_length=200 , null=True , blank=True)
    message_end = models.CharField(max_length=1000)
    message_end_user_id = models.CharField(max_length=20)
    end_time = models.CharField(max_length=200)
    acc_id = models.ForeignKey('Account' , on_delete=models.CASCADE, related_name='account_chats')

    def __str__(self):
        return self.chat_id

class Account_Contacts(models.Model):
    user_id = models.CharField(max_length=20)
    acc_id = models.ForeignKey('Account' , on_delete=models.CASCADE, related_name='account_contacts')
    
    def __str__(self):
        return self.user_id

class Account_Search_Chat(models.Model):
    chat_id = models.CharField(max_length=20)
    acc_id = models.ForeignKey('Account' , on_delete=models.CASCADE, related_name='account_search_chat')
    
    def __str__(self):
        return self.chat_id


# for chat info

class Chat(models.Model):
    id = models.CharField(max_length=20 , primary_key=True)
    name = models.CharField(max_length=40 , null=True , blank=True)
    link = models.CharField(max_length=30 , null=True , blank=True )
    bio = models.CharField(max_length=200 , null=True , blank=True)
    id_create_user = models.CharField(max_length=20)
    id_called_user = models.CharField(max_length=20 , null=True , blank=True)
    img_end = models.CharField(max_length=200 , null=True , blank=True)
    tip = models.CharField(max_length=10)
    time = models.CharField(max_length=20)

    def __str__(self):
        return self.id

class Chat_Img(models.Model):
    link = models.CharField(max_length=200)
    time = models.CharField(max_length=20)
    chat_id = models.ForeignKey('Chat' , on_delete=models.CASCADE, related_name='chat_img')
    
    def __str__(self):
        return self.link

class Chat_Member(models.Model):
    id_member = models.CharField(max_length=20)
    admin = models.CharField(max_length=20 , null=True , blank=True)
    chat_id = models.ForeignKey('Chat' , on_delete=models.CASCADE, related_name='chat_chats')

    def __str__(self):
        return self.id_member

class Chat_Message(models.Model):
    id_member = models.CharField(max_length=20)
    text = models.TextField(max_length=1000 , null=True , blank=True)
    img = models.TextField(max_length=1000 , null=True , blank=True)
    video = models.TextField(max_length=1000 , null=True , blank=True)
    time = models.CharField(max_length=20)
    chat_id = models.ForeignKey('Chat' , on_delete=models.CASCADE, related_name='chat_message')
    
    def __str__(self):
        return self.id_member



