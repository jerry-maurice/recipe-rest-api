from django.db import models
from django.contrib.auth.models import User

# a list of different type of food and drink
class Category(models.Model):
    image = models.URLField(max_length=250, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    # provide a simple description when view this model
    def __str__(self):
        return '{} - {}'.format(self.name, self.description)


# a map of purchasing items. Google Api will be used to locate this place
class Locations(models.Model):
    address = models.CharField(null=True, max_length=250)
    name = models.CharField(null=True, max_length=250)
    place_id = models.CharField(null=True, max_length=250)
    # provide a simple description when view this model
    def __str__(self):
        return self.name


# which country style or cuisine style is this meal
class CuisineStyle(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=False)
    # provide a simple description when view this model
    def __str__(self):
        return self.name


# recipe object to store content of a recipe
class Recipes(models.Model):
    image = models.URLField(max_length=250)
    name = models.CharField(max_length=100)
    description = models.TextField(null=False)
    # check if recipe is a meal or a drink
    is_meal = models.BooleanField(default=True, null=False)
    # Category of food Foreign key
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # style of cuisine
    style = models.ForeignKey(CuisineStyle, on_delete=models.CASCADE, related_name='recipes') 
    # To be changed later. User class required
    made_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False,
                                default=None, related_name='recipes')          
    created = models.DateField(auto_now=True)
    # favorite = models.ManyToManyField(User, through='Favorite')
    # provide a simple description when view this model
    def __str__(self):
        return self.name


# a list of direction
class Directions(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=False)
    lengthOfTime = models.TextField(null=False)
    # link to video
    video = models.URLField(null=True)
    # recipe foreign key
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, null=False,
                               default=None, related_name='directions') 
    # provide a simple description when view this model
    def __str__(self):
        return self.name


# a list of ingredients
class Ingredients(models.Model):
    name = models.CharField(max_length=250)
    size = models.CharField(null=True, max_length=100)
    # showing the place of purchase
    location = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True)
    # recipe foreign key
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, null=False,
                               default=None, related_name='ingredients')
    # provide a simple description when view this model
    def __str__(self):
        return self.name


# reviews
class Reviews(models.Model):
    stars = models.FloatField(default=0)
    created = models.DateField(auto_now=True)
    detail = models.TextField(null=False)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, null=False,
                             default=None, related_name='reviews') 
    # user 
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False,
                             default=None, related_name='reviews')
    # provide a simple description when view this model
    def __str__(self):
        return self.detail
    


# favorite -- the user favorite recipe

class Favorite(models.Model):
    recipe = models.ManyToManyField(Recipes, related_name='favorites')
    #  add user
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites') 
    added =  models.DateField(auto_now=True)
    # provide a simple description when view this model
    def __str__(self):
        return self.added
    
    
