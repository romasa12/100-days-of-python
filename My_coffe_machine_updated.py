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
    "money": 0,
}


def coin():
    print("insert coins: ")
    a=int(input("how many quaters?: "))*0.25
    b=int(input("how many dimes?: "))*0.10
    c=int(input("How many nickles?: "))*0.05
    d=int(input("how many pennies?: "))*0.01
    total=a+b+c+d
    return round(total,2)

cost_e=MENU["espresso"]["cost"]
cost_l=MENU["latte"]["cost"]
cost_c=MENU["cappuccino"]["cost"]
game=True

while game==True:

    user_choice=input("What would you like? (espresso/latte/cappuccino):")  
    if user_choice=="off":
        game=False
    elif user_choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: $ {resources["money"]}")  

    elif user_choice=="espresso" :
        if resources["water"]>MENU["espresso"]["ingredients"]["water"]:
            if resources["coffee"]>MENU["espresso"]["ingredients"]["coffee"]: 
                givin_value=coin()    
                if givin_value>=cost_e:
                    print("“Here is your espresso. Enjoy!")
                    print(f"Here  is $ {givin_value-cost_e} dollars in change ")
                    resources["water"]-=MENU["espresso"]["ingredients"]["water"] 
                    resources["coffee"]-=MENU["espresso"]["ingredients"]["coffee"]
                    resources["money"]+=cost_e
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water")
            
    elif user_choice=="latte":
        if resources["water"]>MENU["latte"]["ingredients"]["water"]:
            if resources["coffee"]>MENU["latte"]["ingredients"]["coffee"]: 
                if resources["milk"]>MENU["latte"]["ingredients"]["milk"]: 
                    givin_value=coin()    
                    if givin_value>=cost_l:
                        print("“Here is your Latte. Enjoy!")
                        print(f"Here  is $ {givin_value-cost_l} dollars in change ")
                        resources["water"]-=MENU["latte"]["ingredients"]["water"] 
                        resources["milk"]-=MENU["latte"]["ingredients"]["milk"]     
                        resources["coffee"]-=MENU["latte"]["ingredients"]["coffee"] 
                        resources["money"]+=cost_l
                else:
                    print("Sorry there is not enough milk")
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water")

    elif user_choice=="cappuccino" :
        if resources["water"]>MENU["cappuccino"]["ingredients"]["water"]:
            if resources["coffee"]>MENU["cappuccino"]["ingredients"]["coffee"]: 
                if resources["milk"]>MENU["cappuccino"]["ingredients"]["milk"]: 
                    givin_value=coin()    
                    if givin_value>=cost_c:
                        print("“Here is your cappuccino. Enjoy!")
                        print(f"Here  is $ {givin_value-cost_c} dollars in change ")
                        resources["water"]-=MENU["cappuccino"]["ingredients"]["water"] 
                        resources["milk"]-=MENU["cappuccino"]["ingredients"]["milk"]     
                        resources["coffee"]-=MENU["cappuccino"]["ingredients"]["coffee"] 
                        resources["money"]+=cost_c
                else:
                    print("Sorry there is not enough milk")
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water")

    else:
        print("Sorry that's not enough money. Money refunded.")
        game=False

        



