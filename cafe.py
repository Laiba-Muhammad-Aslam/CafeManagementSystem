# Menu

menu = {
  "Pizza": 500,
  "Burger": 200,
  "Biryani": 300,
  "Pasta" : 350
}

# GREETINGS 

print("Welcome to our Resturant")

total_amout = 0

item_1 = input("Enter the item you want to order: ")

if item_1 in menu:
    total_amout += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
    choice = input("Do you want to oreder another item? Yes | No ")
    if choice == "Yes":
        item_2 = input("Enter the item you want to order: ")
        if item_2 in menu:
             total_amout += menu[item_2]
             print(f"Your item {item_2} has been added to your order")
        else:
            print(f"Oredred item is not available yet!")             

else:
    print(f"Oredred item is not available yet!")

print(f"Your total bill is {total_amout}")
