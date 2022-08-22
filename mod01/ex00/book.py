import datetime
from recipe import Recipe


class Book:
    def __init__(self, name):
        assert isinstance(name, str), 'name must be a string'
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = self.creation_date
        self.recipe_list = {
            'starter': [],
            'lunch': [],
            'dessert': []
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        assert isinstance(name, str), 'name must be a string'
        for _ in self.recipe_list.values():
            for recipe in _:
                if name == recipe.name:
                    print(recipe)
                    return recipe
        print("The recipe doesn't exists")
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        assert isinstance(recipe_type, str), 'recipe_type must be a string'
        assert recipe_type in {'starter', 'lunch', 'dessert'}, 'recipe_type must be:\
 starter, lunch or dessert'
        return self.recipe_list[recipe_type]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        assert isinstance(recipe, Recipe), 'recipe must be instance of the class Recipe'
        self.last_update = datetime.datetime.now()
        self.recipe_list[recipe.recipe_type].append(recipe)
