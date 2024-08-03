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
def is_resource_sufficent(order_ingredients):
    is_enough=True
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough=False
            return is_enough
    is_enough=True
    return is_enough
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f" Here is your {drink_name}. Enjoy!")
def process_coin():
    print("insert coins: ")
    a=int(input("how many quaters?: "))*0.25
    b=int(input("how many dimes?: "))*0.10
    c=int(input("How many nickles?: "))*0.05
    d=int(input("how many pennies?: "))*0.01

    total=a+b+c+d
    return round(total,2)
 
def is_transaction_successful(money_received,drink_cost):
    if money_received>=drink_cost:
       change=round(money_received-drink_cost,2)
       global profit
       profit+=drink_cost
       print(f"Here is ${change} dollars in change ")
       return True
    else:
       print("Sorry that's not enough money. Money refunded.")
       return False
       
profit=0
is_on=True
while is_on==True:
    choice=input("What would you like? (espresso/latte/cappuccino):")
    if choice=="off":
        print("machine off")
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: $ {profit}")   
    else:
        drink=MENU[choice]    
        if is_resource_sufficent(drink["ingredients"]):
            payment=process_coin()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"]) 