from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions

from recipes.models import Category, Ingredients, Locations, Directions
from recipes.models import Reviews, CuisineStyle, Favorite, Recipes

from recipes.serializers import CategorySerializer, IngredientSerializer
from recipes.serializers import ReviewSerializer, CuisineSerializer
from recipes.serializers import LocationSerializer, DirectionSerializer
from recipes.serializers import RecipeSerializer, FavoriteSerializer
from recipes.serializers import UserSerializer, RecipeLessSerializer, FavoriteFullSerializer

# from social_core.backends.oauth import BaseOAuth1, BaseOAuth2
# from social_core.backends.google import GooglePlusAuth
# from social_core.backends.utils import load_backends
# from social_django.utils import psa, load_strategy



class CategoryList(generics.ListCreateAPIView):
    '''
    List all category or creating new category
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    '''
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)'''
    


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update, or delete a category
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class UserList(generics.ListCreateAPIView):
    '''
    List all category or creating new user
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update, or delete a user
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer



class LocationList(generics.ListCreateAPIView):
    '''
    List all category or creating new lacation
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer
    


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update, or delete a category
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer


class IngredientList(generics.ListCreateAPIView):
    '''
    List all category or creating new ingredient
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer

    

class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update, or delete a ingredient
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer



class DirectionList(generics.ListCreateAPIView):
    '''
    List all category or creating new direction
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Directions.objects.all()
    serializer_class = DirectionSerializer
    


class DirectionDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update, or delete a direction
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Directions.objects.all()
    serializer_class = DirectionSerializer



class CuisineList(generics.ListCreateAPIView):
    '''
    List all category or creating new direction
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CuisineStyle.objects.all()
    serializer_class = CuisineSerializer
    


class CuisineDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update, or delete a direction
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CuisineStyle.objects.all()
    serializer_class = CuisineSerializer



class RecipeList(generics.ListAPIView):
    '''
    List all category or creating new recipe
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    


class RecipeDetail(generics.RetrieveDestroyAPIView):
    '''
    Retrieve, update, or delete a recipe
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer



class RecipeLessList(generics.ListCreateAPIView):
    '''
    List all category or creating new recipe
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipes.objects.all()
    serializer_class = RecipeLessSerializer
    


class RecipeLessDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update, or delete a recipe
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipes.objects.all()
    serializer_class = RecipeLessSerializer



class ReviewList(generics.ListCreateAPIView):
    '''
    List all category or creating new reviews
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update, or delete a reviews
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer



class FavoriteList(generics.ListCreateAPIView):
    '''
    List all category or creating new reviews
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    


class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update, or delete a reviews
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer



class FavoriteUserList(generics.ListCreateAPIView):
    '''
    List all category or creating new reviews
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(author=user)
    


class FavoriteUserDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update, or delete a reviews
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(author=user)



class FavoriteFullUserList(generics.ListAPIView):
    '''
    List all category or creating new reviews
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteFullSerializer

    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(author=user)
    


class FavoriteFullUserDetail(generics.RetrieveDestroyAPIView):
    '''
    Retrieve, update, or delete a reviews
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteFullSerializer

    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(author=user)



class UserRecipeList(generics.ListAPIView):
    '''
    List all the recipe of the user who created it
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        user = self.request.user
        return Recipes.objects.filter(made_by=user)



class UserRecipeDetail(generics.RetrieveDestroyAPIView):
    '''
    retrieve and delete the recipes of the user who created it
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        user = self.request.user
        return Recipes.objects.filter(made_by=user)





    
