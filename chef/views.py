from django.shortcuts import render
from rest_framework import viewsets, filters , pagination,permissions
from .import serializers
from rest_framework.decorators import action,api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Chef,Recipe,Event
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

class ChefPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = page_size
    max_page_size = 100


class ChefViewset(viewsets.ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = serializers.ChefSerializers
    filter_backends = [filters.SearchFilter]
    pagination_class = ChefPagination
    # search_fields = ['user__first_name', 'user__email']
    
class RecipeForSpecificChef(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        chef_id = request.query_params.get("chef_id")
        if chef_id:
            return query_set.filter(chef = chef_id)
        return query_set

class RecipeViewset(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [RecipeForSpecificChef]




class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = serializers.EventSerializers
  

