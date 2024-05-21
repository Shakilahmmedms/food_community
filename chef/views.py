from django.shortcuts import render
from rest_framework import viewsets, filters , pagination,permissions
from .import serializers
from rest_framework.decorators import action,api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Chef,Recipe,Event, User
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

# Create your views here.

# class ChefPagination(pagination.PageNumberPagination):
#     page_size = 1
#     page_size_query_param = page_size
#     max_page_size = 100


class ChefViewset(viewsets.ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = serializers.ChefSerializers
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user = user)

    @action(detail=False, methods=['get'])
    def get_chef_data(self, request):
        serializer = self.get_serializer(request.user.chef)
        return Response(serializer.data)
    

class RecipeViewset(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializers
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        recipes = self.get_queryset()
        serializer = self.get_serializer(recipes, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = serializers.EventSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        organizer = self.request.user.chef
        serializer.save(organizer=organizer)



class RegisterUser(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        is_chef = request.data.get('is_chef', False)

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        
        if is_chef:
            Chef.objects.create(user=user)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)



