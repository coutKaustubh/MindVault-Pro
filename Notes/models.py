from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    user = models.ForeignKey(User,  on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Entry(models.Model):
    user = models.ForeignKey(User,  on_delete=models.SET_NULL,null=True,blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='entries')
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='entries/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic.name} → {self.title}"
