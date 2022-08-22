class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        assert isinstance(name, str), 'name must be a string'
        assert isinstance(cooking_lvl, int), 'cooking_lvl must be an integer'
        assert 1 <= cooking_lvl and cooking_lvl <= 5, 'cooking_lvl must be between 1 <= x <= 5'
        assert isinstance(cooking_time, int), 'cooking_time must be an integer'
        assert cooking_time >= 0, 'cooking_time must be positive'
        assert isinstance(ingredients, list), 'ingredients must be a list'
        assert len(ingredients) > 0, "ingredient's list must not be empty"
        for _ in ingredients:
            assert isinstance(_, str), "ingredient's list elements must be strings"
        assert isinstance(description, str) or description == None, 'description must be a string'
        assert isinstance(recipe_type, str), 'recipe_type must be a string'
        assert recipe_type in {'starter', 'lunch', 'dessert'}, 'recipe_type must be:\
 starter, lunch or dessert'
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        return f'Recipe({self.name}, {self.description}, {self.ingredients})'
