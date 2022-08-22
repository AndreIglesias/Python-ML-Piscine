from recipe import Recipe
from book import Book


if __name__ == '__main__':
    try:
        o = Recipe("cooki", 0, 10, ["dough", "sugar", "love"], "deliciousness incarnate", "dessert")
        print(str(o))
    except AssertionError as msg:
        print("AssertionError:", msg)
    try:
        o = Recipe("cooki", 1, 10, ["dough", "sugar", "love"], "deliciousness incarnate", "dessert")
        o1 = Recipe("budin", 1, 10, ["dough", "sugar", "love"], "deliciousness incarnate", "dessert")
        b = Book("booki")
        print(b.creation_date)
        print(b.last_update)
        b.add_recipe(o)
        b.add_recipe(o1)
        print(b.last_update)
        print(b.get_recipes_by_types("dessert")[0])
        b.get_recipe_by_name("cookif")
    except AssertionError as msg:
        print("AssertionError:", msg)
