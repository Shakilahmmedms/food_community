from rest_framework import serializers
from .models import Chef,Recipe,Event, User


class ChefSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ['id', 'name', 'bio', 'recipes']


class RecipeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'ingredients', 'instructions', 'creation_date', 'image_url']

class EventSerializers(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'date', 'location']






    
