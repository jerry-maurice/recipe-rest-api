from django.urls import path, include
# from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns = [
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    
    # recipes path
    path('categories/', views.CategoryList.as_view(), name='categoryList'),
    path('categories/<int:pk>', views.CategoryDetail.as_view(),
         name='categoryDetail'),
    path('locations/', views.LocationList.as_view(), name='locationList'),
    path('locations/<int:pk>', views.LocationDetail.as_view(),
         name='locationDetail'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredientList'),
    path('ingredients/<int:pk>', views.IngredientDetail.as_view(),
         name='ingredientDetail'),
    path('directions/', views.DirectionList.as_view(), name='directionList'),
    path('directions/<int:pk>', views.DirectionDetail.as_view(),
         name='directionDetail'),
    path('cuisine/', views.CuisineList.as_view(), name='cuisineList'),
    path('cuisine/<int:pk>', views.CuisineDetail.as_view(),
         name='cuisineDetail'),
    path('recipes/', views.RecipeList.as_view(), name='recipeList'),
    path('recipes/<int:pk>', views.RecipeDetail.as_view(),
         name='recipeDetail'),
    path('recipes-less/', views.RecipeLessList.as_view(), name='recipeLessList'),
    path('recipes-less/<int:pk>', views.RecipeLessDetail.as_view(),
         name='recipeLessDetail'),
    path('reviews/', views.ReviewList.as_view(), name='reviewsList'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(),
         name='reviewsDetail'),
    path('favorites/', views.FavoriteList.as_view(), name='favoriteList'),
    path('favorites/<int:pk>', views.FavoriteDetail.as_view(),
         name='favoriteDetail'),
    path('favorites-user/', views.FavoriteUserList.as_view(), name='favoriteUserList'),
    path('favorites-user/<int:pk>', views.FavoriteUserDetail.as_view(),
         name='favoriteUserDetail'),
    path('favorites-full-user/', views.FavoriteFullUserList.as_view(), name='favoriteFullUserList'),
    path('favorites-full-user/<int:pk>', views.FavoriteFullUserDetail.as_view(),
         name='favoriteFullUserDetail'),
    path('user-recipes/', views.UserRecipeList.as_view(), name='user-recipe'),
    path('user-recipes/<int:pk>', views.UserRecipeDetail.as_view(), name='user-recipeDetail'),
    
    # browsable API
    path('api-auth/', include('rest_framework.urls')),
    #path('api/login/', include('rest_social_auth.urls_token')),
    #path('login/', views.login, name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name = "logout"),
    ]


urlpatterns = format_suffix_patterns(urlpatterns)
