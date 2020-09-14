import requests

def recipe_search(ingredient, health, excluded):
    app_id = 'fcc37625'
    app_key = 'a72e84a27e33af05a276b87129a54cdc'
    if health == "" or 'no':
        result = requests.get(
'https://api.edamam.com/search?q={}&app_id={}&app_key={}&excluded={}'.format(ingredient, app_id, app_key, excluded)
    )
    elif excluded == "" or 'no':
        result = requests.get(
'https://api.edamam.com/search?q={}&app_id={}&app_key={}&health={}'.format(ingredient, app_id, app_key, health)
    )
    elif excluded and 'health' == "" or 'no':
        result = requests.get(
'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    )
    else:
        result = requests.get(
'https://api.edamam.com/search?q={}&app_id={}&app_key={}&health={}&excluded={}'.format(ingredient, app_id, app_key, health, excluded)
        )

    data = result.json()
    return data['hits']


def run():
    ingredient = input('Enter an ingredient? ')
    health = input('Any dietary/health requirements? ')
    excluded = input('Any allergens? ')

    results = recipe_search(ingredient, health, excluded)

    output = ''

    for result in results:
        recipe = result['recipe']
        output += "\n"
        output += recipe['label']
        output += "\n"
        output += "Calories: {}".format(int(recipe['calories']))
        output += "\n"
        output += "Link: {}".format(recipe['shareAs'])
        output += "\n"
    number_recipe = len(results)
    print(f"Your search produced {number_recipe} recipes. Detailed results are shown in the recipes file.")
    return output

with open('recipes.txt', 'w') as output_recipe:
    output_recipe.write(run())