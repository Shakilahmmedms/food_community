from rest_framework import serializers
from .models import Chef,Recipe,Event, User
from rest_framework.authtoken.models import Token



    

class ChefSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ['id', 'username', 'bio', 'recipes']


class RecipeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = '__all__'

class EventSerializers(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'






    
