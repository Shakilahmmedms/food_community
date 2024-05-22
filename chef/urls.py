from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('chefs', views.ChefViewset)
router.register('recipes', views.RecipeViewset)
router.register('events', views.EventViewset)

urlpatterns = [
    path('', include(router.urls)),
   
]