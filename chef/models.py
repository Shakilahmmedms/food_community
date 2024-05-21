from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

class Chef(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='chef_profile')
    bio = models.TextField()
    

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}" 


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300,null=True, blank=True)
    instruction = models.CharField(max_length=100,null=True, blank=True)
    ingredients = models.CharField(max_length=200,null=True, blank=True)
    created = models.DateField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to='chef/images/', default='default_image.jpg')
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.chef.user.first_name}"
    
class Event(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField()
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(Chef, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.organizer.user.first_name}"