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

coins_names = ['quarters', 'dimes', 'nickles', 'pennies']

coins_values = {
    'quarters': 0.25,
    'dimes': 0.1,
    'nickles': 0.05,
    'pennies': 0.01
}

coffee_machine_inserted_money = 0


def is_transaction_successful(total_sum, drink_price):
    if total_sum < drink_price:
        print(f"Sorry that's not enough money. Money refunded.")
        return False
    if total_sum == drink_price:
        return True
    if total_sum > drink_price:
        change = total_sum - drink_price
        print(f"Here is ${change:.2f} dollars in change.")
        return True


def calc_coins_value(coins_count_dict):
    result = 0
    for c_name, c_value in coins_count_dict.items():
        result += coins_values[c_name] * c_value

    return result


def process_coins(drink_price):
    print('Please insert coins.')
    coin_values = {}
    for c in coins_names:
        question = int(input(f"How many {c}?: "))
        # coin_values.append(question)
        coin_values[c] = question
    total_sum = calc_coins_value(coin_values)
    if is_transaction_successful(total_sum, drink_price):
        # coffee_machine_inserted_money += drink_price
        return True
    return False


def check_resources(ingredients):
    drink_ingredients = ingredients['ingredients']

    for product, quantity in resources.items():
        if product not in drink_ingredients:
            continue
        if quantity < drink_ingredients[product]:
            print(f"Sorry there is not enough {product}.")
            print(f"Try with another drink.")
            return False
    return True


def decrease_products(ingredients):
    for product, quantity in ingredients.items():
        resources[product] -= quantity
    return True


out_of_stock_orders = []


def make_drink(drink):
    for d, v in MENU.items():
        if d == drink:
            drink_price = v['cost']
            if check_resources(v):
                if process_coins(drink_price):
                    decrease_products(v['ingredients'])

                    print(f"Here is your {drink}. Enjoy!")

                    return True

    return False


while True:
    offer = input(" What would you like? (espresso/latte/cappuccino): ")
    if offer == 'report':
        for k, v in resources.items():
            print(f"{k.capitalize()}: {v}ml")
        print(f"Money: ${coffee_machine_inserted_money}")
    elif offer == 'off':
        break
    else:
        temp = make_drink(offer)
        if temp is True:
            drink_price = MENU[offer]['cost']
            coffee_machine_inserted_money += drink_price
            continue
        if temp is False:
            out_of_stock_orders.append(offer)
            if len(out_of_stock_orders) == 3:
                print(f"Sorry, soon the products will be restocked.")
                break
