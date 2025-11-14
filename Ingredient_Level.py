# STEP 5 — Stock Level Tracker
# =======================================

# takes the daily order that will be inputed into the csv tracker and calculates the amount of ingredients used in that day

from Ingredients import parse_amount
from Dishes import dishes
from Input_Checker import input_day_orders

def day_ingredient_use (day_orders):
  dishes_sold=input_day_orders(day_orders)["stir fry noodles"] # goes through a checker function that returns solely the dishes consumed and their amount if and only if dish is in menu
  inv_loss=[]

  for ing in dishes['stir fry noodles'].keys(): # goes through every ingredient used for the dish ordered (we only have 1 for MVP), parses quantity and adds just the base units to a list
    ing_loss=parse_amount(dishes['stir fry noodles'][ing])[0]*dishes_sold # multiplies by number of dishes ordered
    inv_loss.append(ing_loss)

  return(inv_loss) # return the amount of ingredients lost in the day, sorted based on order of ceation of the dish


# Function: takes the daily order and initial dictionary of igredients and subtracts them to have the remaining amouunt of ingredients left

def ingredient_tracker (current_ingredients, day_orders, original_stock):
  inv_loss=day_ingredient_use(day_orders) # call "day_ingredient_use" to find how much ingredients was used
  ing_order = list(dishes['stir fry noodles'].keys()) # creates a list of the ingredients used for our MVP dish, done to keep a general order

  current_amount=[]
  current_units=[]
  updated=[]

  import copy
  copy_ingredients=copy.deepcopy(current_ingredients) # creates a copy of original dictionary of ingredients to not change it

  for name in ing_order: # checks for the current amount of ingredients and separates the units and numbers into different lists
        val, unit = parse_amount(current_ingredients[name]["amount"])
        current_amount.append(val)
        current_units.append(unit)

  for i in range(len(ing_order)): # subtracts the ingredients used by order from the current amount
    new=current_amount[i]-inv_loss[i]
    if new<=0: # to avoid negative stock levels
      updated.append(0)
    else:
      updated.append(new)

  for name, val, unit in zip(ing_order, updated, current_units): # puts the updated quantoty back together with the units
      copy_ingredients[name]["amount"] = f"{val} {unit}"

  for i in range(len(updated)): # goes through every quantity of the updated ingredients and checks if its 20% of the original amount (first time inputed --> when purchase is done)
      og_amount = parse_amount(original_stock[ing_order[i]]["amount"])[0]
      if og_amount > 0:  # avoid division by zero
          per_cent = updated[i] / og_amount
          if per_cent <= 0.2:
              print(f"You must reorder {ing_order[i]} (only {per_cent*100:.1f}% left)")

  return copy_ingredients # returns the new uopdated dictionary


