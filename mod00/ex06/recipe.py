cookbook = {
    'sandwich' : {
        'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal' : 'lunch',
        'prep_time' : 10
    },
    'cake' : {
        'ingredients' : ['flour', 'sugar', 'eggs'],
        'meal' : 'dessert',
        'prep_time' : 60
    },
    'salad' : {
        'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal' : 'lunch',
        'prep_time' : 15
    }
}

def recipe_names():
    global cookbook
    [print(' - ' + name) for name in cookbook.keys()]

def recipe_details(recipe):
    if recipe in cookbook.keys():
        print('Recipe for' + recipe + ':')
        print('   Ingredients list:', cookbook[recipe]['ingredients'])
        print('   To be eaten for', cookbook[recipe]['meal'])
        print('   Takes', cookbook[recipe]['prep_time'], 'minutes of cooking')
    else:
        print('N/A')

def delete_recipe(recipe):
    if recipe in cookbook.keys():
        cookbook.pop(recipe)
    else:
        print('N/A')

def enter_recipe():
    global cookbook
    name = input('>>> Enter a name:\n')
    cookbook[name] = {}
    ingredients = []
    ingredient = '_'
    print('>>> Enter ingredients:')
    while ingredient != '':
        ingredient = input()
        ingredients.append(ingredient)
    cookbook[name]['ingredients'] = ingredients
    cookbook[name]['meal'] = input(">>> Enter a meal type:\n")
    cookbook[name]['prep_time'] = input('>>> Enter a preparation time:\n')

fn = [enter_recipe, delete_recipe, recipe_details, recipe_names, exit]

if __name__ == '__main__':
    print('Welcome to the Python Cookbook !')
    print('List of available option:')
    print('   1: Add a recipe', '   2: Delete a recipe', sep='\n')
    print('   3: Print a recipe', '   4: Print the cookbook', sep='\n')
    print('   5: Quit\n')
    while True:
        print('Please select an option:')
        op = input('>> ')
        print()
        if op in {'1', '2', '3', '4', '5'}:
            if op in {'2', '3'}:
                print('Please enter a recipe name:')
                name = input('>> ')
                print()
                fn[int(op) - 1](name)
            else:
                if op == '5':
                    print('Cookbook closed. Goodbye!')
                fn[int(op) - 1]()
            print()
        else:
            print('Sorry, this option does not exist.')
            print('List of available option:')
            print('   1: Add a recipe', '   2: Delete a recipe', sep='\n')
            print('   3: Print a recipe', '   4: Print the cookbook', sep='\n')
            print('   5: Quit\n')
