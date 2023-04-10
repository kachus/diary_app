from django.db import models

# Create your models here.
class User(models.Model):
    id = models.BigAutoField('id', primary_key=True)
    #user_id = from telegram. PK
    username = models.CharField('username',max_length=100)
    #firstname = models.CharField(max_length=100, null=True)
    #lastname = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    situation = models.TextField()
    thoughts = models.TextField()
    emotions = models.TextField()
    conclusion = models.TextField()
    def __str__(self):
        return str(self.user.username)



