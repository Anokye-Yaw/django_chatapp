from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name  

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True) #datetime changes any time you update
    created = models.DateTimeField(auto_now_add=True)#datetime does not change once  datetime created
    
    class Meta:
        ordering = ['-updated', '-created'] #desending order because of - sign of(updated and created)
    
    def __str__(self):
        return self.name
    
    
class Message(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) #datetime changes any time you update
    created = models.DateTimeField(auto_now_add=True)#datetime does not change once  datetime created
    
    def __str__(self):
        return self.body[0:50]    