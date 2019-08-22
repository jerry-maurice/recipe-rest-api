from rest_framework import serializers
from recipes.models import Category, Ingredients, Locations, Directions, Recipes
from recipes.models import Reviews, CuisineStyle, Favorite

from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    '''
        displaying user info
    '''
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'image','name', 'description']
        owner = serializers.ReadOnlyField(source='owner.username')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ['id', 'address', 'name', 'place_id']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['id', 'name', 'size', 'location', 'recipe']


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directions
        fields = ['id', 'name', 'description', 'lengthOfTime', 'video', 'recipe']


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuisineStyle
        fields = ['id', 'name', 'description']



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'stars', 'created', 'detail','recipe', 'author']



class ReviewDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Reviews
        fields = ['id', 'stars', 'created', 'detail', 'author']



class RecipeSerializer(serializers.ModelSerializer):
    made_by = UserSerializer()
    ingredients = IngredientSerializer(many=True)
    directions = DirectionSerializer(many=True)
    style = CuisineSerializer()
    category = CategorySerializer()
    reviews = ReviewDetailSerializer(many=True)
    class Meta:
        model = Recipes
        fields = ['id', 'image', 'name', 'description', 'is_meal', 'category',
                  'style', 'made_by', 'created', 'ingredients', 'directions',
                  'reviews']


'''
    Not enough detail provided
'''
class RecipeLessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['id', 'image', 'name', 'description', 'is_meal', 'category',
                  'style', 'made_by', 'created']



class FavoriteSerializer(serializers.ModelSerializer):
    # recipe = RecipeLessSerializer(many=True)
    class Meta:
        model = Favorite
        fields = ['id', 'author', 'added', 'recipe']



class FavoriteFullSerializer(serializers.ModelSerializer):
    recipe = RecipeLessSerializer(many=True)
    class Meta:
        model = Favorite
        fields = ['id', 'author', 'added', 'recipe']
