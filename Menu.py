# Objective - for the user to select 3 of their favourite foods from a menu and get an order comfirmation
# Create a welcoming greeting
print("Welcome to Tom's Restuarant, Please see the menu below!")
print()
# print a menu with the food choices
menu = ("menu \n Pepperoni Pizza \n Steak and Chips \n Pie \n Chicken Nuggets \n Lasange \n Spaghetti Bolognase \n Sausage and Mash")
print(menu)
print()
# ask the user what 3 foods they would like to order
first_favourite_food = input("What is your first choice? ")
print()
second_favourite_food = input("What is your second choice? ")
print()
third_favourite_food = input("What is your third choice? ")
print()
# send comfirmation of there order.
print("Order Confirmed, Thanks for ordering with us!")
print(first_favourite_food)
print(second_favourite_food)
print(third_favourite_food)