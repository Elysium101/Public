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

machine_on = True
money = 0.0
not_enough = "I'm sorry, you have not entered enough money"

# format the resources for the report option
def format_resources():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")

# Once there is enough resources, calculate the cost against how much has been entered into the machine.
# Then, once the transaction is successful, work out the change and update the money variable for the revenue
def money_check():
    global money
    print('Please insert your coins:')
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies: "))
    quarters_total = quarters * 0.25
    dimes_total = dimes * 0.10
    nickles_total = nickles * 0.05
    pennies_total = pennies * 0.01
    total = quarters_total + dimes_total + nickles_total + pennies_total
    if choice == 'espresso':
        if total > MENU['espresso']['cost']:
            change = total - MENU['espresso']['cost']
            revenue = MENU['espresso']['cost']
            money += revenue
            print(f"Thanks, enjoy your {choice.title()}! Here is your change: ${change:.2f}.")
        else:
            print(not_enough)
    elif choice == 'latte':
        if total > MENU['latte']['cost']:
            change = total - MENU['latte']['cost']
            revenue = MENU['latte']['cost']
            money += revenue
            print(f"Thanks, enjoy your {choice.title()}! Here is your change: ${change:.2f}.")
    else:
        if total > MENU['cappuccino']['cost']:
            change = total - MENU['cappuccino']['cost']
            revenue = MENU['cappuccino']['cost']
            money += revenue
            print(f"Thanks, enjoy your {choice.title()}! Here is your change: ${change:.2f}.")

# Check the resources available to make sure there is enough of each to fulfill the order.
def resource_check():
    if choice == 'espresso':
        if resources['water'] > MENU['espresso']['ingredients']['water']:
            if resources['milk'] > MENU['espresso']['ingredients']['coffee']:
                money_check()
            else:
                print("Sorry, there is not enough Milk!")
        else:
            print(f"Sorry, there is not enough Water!")
    elif choice == 'latte':
        if resources['water'] > MENU['latte']['ingredients']['water']:
            if resources['milk'] > MENU['latte']['ingredients']['milk']:
                if resources['coffee'] > MENU['latte']['ingredients']['coffee']:
                    money_check()
                else:
                    print("Sorry, there is not enough Coffee")
            else:
                print("Sorry, there is not enough Milk!")
        else:
            print("Sorry, there is not enough Water!")
    elif choice == 'cappuccino':
        if resources['water'] > MENU['cappuccino']['ingredients']['water']:
            if resources['milk'] > MENU['cappuccino']['ingredients']['milk']:
                if resources['coffee'] > MENU['cappuccino']['ingredients']['coffee']:
                    money_check()
                else:
                    print("Sorry, there is not enough Coffee")
            else:
                print("Sorry, there is not enough Milk!")
        else:
            print("Sorry, there is not enough Water!")

# Main program loop
while machine_on:
    choice = input(f"What would you like to drink? Espresso, Latte or Cappuccino: ").lower()
    if choice == 'off':
        machine_on = False
    elif choice == 'report':
       format_resources()
    elif choice in ['latte', 'cappuccino', 'espresso']:
        resource_check()
    else:
        print("It doesnt look like we stock that drink, please try again.")
