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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def order(beverage):
    """ORDER ng customer"""
    if beverage == "espresso":
        return MENU["espresso"]
    if beverage == "latte":
        return MENU["latte"]
    if beverage == "cappuccino":
        return MENU["cappuccino"]


def price(pera):
    """PRICE of order ng customer"""
    if pera == "espresso":
        return MENU["espresso"]["cost"]
    if pera == "latte":
        return MENU["latte"]["cost"]
    if pera == "cappuccino":
        return MENU["cappuccino"]["cost"]


def resource(original, want):
    if want is None:
        return "Invalid selection. Please choose espresso, latte, or cappuccino."
    if original["water"] < want["ingredients"]["water"]:
        return "Sorry there is not water"
    if want != MENU["espresso"]:
        if original["milk"] < want["ingredients"]["milk"]:
            return "Sorry there is not enough milk"

    if original["coffee"] < want["ingredients"]["coffee"]:
        return "Sorry there is not enough coffee"
    return None

def total(q, d, n, p):
    """TOTAL money of customer"""
    q = q*.25
    d = d*.1
    n = n*.05
    p = p*.01
    return q + d + n + p


stop = False
while not stop:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink == "off":
        stop = True

    if drink == "report":
        print(resources)

    gusto = order(drink)
    insufficient_resource = resource(resources,gusto)
    drink_price = price(drink)
    profit = 0

    if not insufficient_resource:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        total_amount = total(quarters, dimes, nickles, pennies)
        if drink_price > total_amount:
            print("Sorry that's not enough money. Money refunded.")
            stop = True
        else:
            print(f"Here is {round(total_amount - drink_price, 2)} dollars in change")
            profit += total_amount
            resources["profit"] = round(profit,2)








