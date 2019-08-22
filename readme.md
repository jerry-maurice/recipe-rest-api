# Recipe Rest Api

Application name: Recipe rest api
Created  by Jerry Maurice

# Description
This application is written in Python,  more pricisely python 3.7. It is a rest project that use the Django Rest Framework. The goal of this project is to provide a backend for the client application. 
Any user can access this api but only an authenticated on can add, update and delete an item. It allows a user to be authenticated using google and facebook. It allows saving and displaying of a list of recipes created by multiple users. Once accessed on the client side , each user has the ability  to  save one or multiple recipes has favorite.
Each recipe is composed of a description, style of cuisine, ingredients, directions, and the user who added that recipe. The list of ingredients may also  provide the locations where it can be purchased. The size needed is also part of the ingredient table. Each direction provided by the user has a length of time.
Each recipe can be place in one or multiple categories. A recipe can be a salad and be vegetable at the same time.
The viewer has the possibility to see all the reviews of a recipe but only an authenticated one can add a review.

# Api Endpoint
- Admin 

admin/


- Authentication

api/v1/ auth/


- recipe endpoint

api/v1/ users/

api/v1/ users/<int:pk>/

api/v1/ categories/ [name='categoryList']

api/v1/ categories/<int:pk> [name='categoryDetail']

api/v1/ locations/ [name='locationList']

api/v1/ locations/<int:pk> [name='locationDetail']

api/v1/ ingredients/ [name='ingredientList']

api/v1/ ingredients/<int:pk> [name='ingredientDetail']

api/v1/ directions/ [name='directionList']

api/v1/ directions/<int:pk> [name='directionDetail']

api/v1/ cuisine/ [name='cuisineList']

api/v1/ cuisine/<int:pk> [name='cuisineDetail']

api/v1/ recipes/ [name='recipeList']

api/v1/ recipes/<int:pk> [name='recipeDetail']

api/v1/ recipes-less/ [name='recipeLessList']

api/v1/ recipes-less/<int:pk> [name='recipeLessDetail']

api/v1/ reviews/ [name='reviewsList']

api/v1/ reviews/<int:pk> [name='reviewsDetail']

api/v1/ favorites/ [name='favoriteList']

api/v1/ favorites/<int:pk> [name='favoriteDetail']

api/v1/ favorites-user/ [name='favoriteUserList']

api/v1/ favorites-user/<int:pk> [name='favoriteUserDetail']

api/v1/ favorites-full-user/ [name='favoriteFullUserList']

api/v1/ favorites-full-user/<int:pk> [name='favoriteFullUserDetail']

api/v1/ user-recipes/ [name='user-recipe']

api/v1/ user-recipes/<int:pk> [name='user-recipeDetail']