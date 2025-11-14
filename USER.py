# first gotta import all the functions








# This is needed for the Ingredient_LEVEL to work

original_stock = copy.deepcopy(ingredients) # right after the ingredient list
current_inventory = copy.deepcopy(ingredients) # right after the ingredient list

current_inventory = ingredient_tracker(current_inventory, day_orders, original_stock) #updates everytime tracker is used cuz it subtracts stuff







# This is from Input_Checker

order1 = {
    "Stir Fry Noodles": "10",     # can convert "10" to float
    "Unknown Dish": 3             # will be skipped (not in dishes)
}

order2 = {
    "Stir Fry Noodles": "hello",  # will be skipped (hello cannot be converted to a float)
    "stir FRY nOOdles": 3         # lower()
}

day1=input_day_orders(order1)
day2=input_day_orders(order2)
print(day1)







# This is from Dishes

add_dish("stir fry noodles", {
    "noodles": "200 g", # already in base units so no need to call the function again
    "chicken": "100 g",
    "carrot": "1 unit",
    "broccoli": "50 g",
    "bell pepper": "40 g"
})

# Print dishes nicely
print("\nDISHES STORED:")
for dish, ingredient_list in dishes.items():
    print(dish, ":", ingredient_list)








# This is from Ingredients

add_ingredient("noodles", "20 kg", 60.0)
add_ingredient("chicken", "10 kg", 90.0)
add_ingredient("carrot", "50 units", 20.0)
add_ingredient("broccoli", "10 kg", 30.0)
add_ingredient("bell pepper", "10 kg", 40.0)












# This is from Cost_tracker

print(calculate_daily_expenses(day1))
print(calculate_daily_expenses(day2))
save_daily_orders_detailed_csv("2026-05-19",day1)