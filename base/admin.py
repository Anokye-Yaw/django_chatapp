from django.contrib import admin

from .models import Room, Topic, Message

# Register your models here.
admin.site.register(Room) # This add Room class inside model.py to django admin panel (127.0.0.1:8000/admin)
admin.site.register(Topic)
admin.site.register(Message)