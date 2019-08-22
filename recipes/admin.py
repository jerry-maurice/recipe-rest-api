from django.contrib import admin

from recipes.models import Category, Ingredients, Locations, Directions, Recipes
from recipes.models import Reviews, CuisineStyle

# Register your models here.
admin.site.register(Category)
admin.site.register(Ingredients)
admin.site.register(Locations)
admin.site.register(Directions)
admin.site.register(Recipes)
admin.site.register(Reviews)
admin.site.register(CuisineStyle)
