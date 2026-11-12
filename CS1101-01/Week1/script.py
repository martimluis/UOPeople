# Café order program
# Menu prices (float) and availability (bool)
menu_prices = {"cappuccino": 5.00, "espresso": 2.50, "latte": 4.50}
menu_available = {"cappuccino": True, "espresso": True, "latte": False}

# Show the menu
print("----- Café Menu -----")
for name in menu_prices:
    status = "Available" if menu_available[name] else "Sold out"
    print(f"{name.title():<12} ${menu_prices[name]:.2f}  ({status})")
print("---------------------")

# 1. Ask the user for input
customer_name = input("Enter your name: ")
item = input("Which item would you like? ").strip().lower()
quantity = int(input("How many would you like? "))  # convert text to int

# 2. Calculate the total cost
if item in menu_prices and menu_available[item]:
    price = menu_prices[item]
    total_cost = 0.0
    total_cost += price * quantity  # assignment operator +=

    # 3. Display a formatted message
    print(f"Customer {customer_name} is buying {quantity} cups of {item}. "
          f"Total cost: ${total_cost:.2f}")
else:
    print(f"Sorry, {item} is not available today.")