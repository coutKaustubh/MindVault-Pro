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
    image = models.FileField(upload_to='entries/', blank=True, null=True)
    PROBLEM_TYPE_CHOICES = [
        ('silly', 'Silly Mistake'),
        ('big', 'Big Mistake'),
        ('concept', 'Conceptual Error'),
        ('calc', 'Calculation Mistake'),
        ('skip', 'Skipped/Unattempted'),
    ]
    problem_type = models.CharField(
        max_length=10,
        choices=PROBLEM_TYPE_CHOICES,
        default='silly'
    )

    PRIORITY_CHOICE = [
        ('high', 'High'),
        ('medium' ,'Medium'),
        ('low','Low'),
    ]
     
    priority_choice = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICE,
        default='medium'
    )
    
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"{self.topic.name} → {self.title}->{self.problem_type}"
  
  
class Notifications(models.Model):
    user = models.ForeignKey(User,  on_delete=models.SET_NULL,null=True,blank=True)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)  
    