from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=225,blank=True,null=True)
    content = models.TextField(max_length=300,blank=True,null=True,help_text='Commens Please')
    pub_date = models.DateField(auto_created=True,null=True,blank=True)
    profile_pic = models.ImageField(upload_to='media/profile_pics/',default='',blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-pub_date']
        