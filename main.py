#listiung all items with their prices
# This script lists all available items with their prices in a restaurant menu format.
items = {
    "samosa":20,
    "biryani": 30,
    "paneer": 25,
    "chicken": 40,
    "fish": 35,
    "salad": 15,
    "soup": 10,
    "dessert": 20,  
}
# Printing the menu items with their prices
print( "samosa:20\n""biryani:30\n""paneer:25\n""chicken:40\n""fish:35\n""salad:15\n""soup:10\n""dessert:20")

price = 0
# Asking the user for their order and checking if it's available
# Taking the first order from the user

user1 = input("What do you want to order? ")

# Checking if the first item is available and calculating the price

if user1 in items:
    price += items[user1]
    print(f"{user1} is available for {price} rupees.")

# If the first item is not available, it will print a message

else:
     print(f"Sorry, {user1} is not available.")
    price1 = 0

# Asking for another order and checking if it's available

user2 = input("What else do you want to order? ")

# Checking if the second item is available and calculating the total price

if user2 in items:
    price2 = items[user2] + items[user1]
    print(f"{user2} is available and total order price is {price2} rupees.")

# If the second item is not available, it will print the total price of the first item

else:
    print(f"Sorry, {user2} is not available.")
    print(f"Your total order price is {price1} rupees.")
