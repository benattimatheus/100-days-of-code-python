MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_enough_resources(order_ingredients):
    """Returns True when order can be made and
    False if there isn't enough resources"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough{item}")
            return False
    return True


def paid_coins():
    """Returns the total from coins inserted"""
    print("Please insert coins")
    total = int(input("How many quarters? "))*0.25
    total += int(input("How many dimes? "))*0.10
    total += int(input("How many nickles? "))*0.05
    total += int(input("How many pennies? "))*0.01
    return total


def transaction(money_received, drink_cost):
    """Returns True and change if the money is enough to pay the drink or
    False if there is not enough money"""
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Uses the drink to update the resources and serve the drink"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml\n")
        print(f"Milk: {resources['milk']}ml\n")
        print(f"Coffee: {resources['coffee']}g\n")
        print(f"Money: ${profit}\n")
    else:
        drink = MENU[choice]
        if is_enough_resources(drink["ingredients"]):
            payment = paid_coins()
            if transaction(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
