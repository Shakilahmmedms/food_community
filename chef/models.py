from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User



class Chef(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(blank=True)
    



class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300,null=True, blank=True)
    instruction = models.CharField(max_length=100,null=True, blank=True)
    ingredients = models.CharField(max_length=200,null=True, blank=True)
    created = models.DateField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to='chef/images/')
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE,related_name='recipes')

    def __str__(self):
        return f"{self.title} "
    
class Event(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField()
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(Chef, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"