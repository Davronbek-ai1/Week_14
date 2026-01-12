def check_ingredients(pantry_list, recipe_list):
    pantry_set = {item.lower() for item in pantry_list}
    recipe_set = {item.lower() for item in recipe_list}
    missing_list = list(recipe_set - pantry_set)
    available_list = list(pantry_set & recipe_set)
    (missing_list and available_list).sort()
    return missing_list, available_list

pantry = ["Eggs", "flour", "Milk", "eggs", "salt"]
recipe = ["flour", "milk", "Sugar", "Eggs", "butter"]

missing, available = check_ingredients(pantry, recipe)

print(f"Need to buy: {missing}")
print(f"Already have: {available}")