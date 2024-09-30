import data

def turnOn():
    print("Turning On...")
    coffeeMachinefunc()

def turnOff():
    print("Shutting down, Goodbye")



def printReport():
    water=data.resources["water"]
    milk=data.resources["milk"]
    coffee=data.resources["coffee"]
    money=data.resources["money"]
    print(f"Water:{water}ml\nMilk:{milk}ml\nCoffee:{coffee}g\nMoney:${money}\n")

def fillMachine():
    data.resources["water"]=300
    data.resources["milk"]=200
    data.resources["coffee"]=100
    printReport()

def makeCoffee(i_coffee):
    """Returns true if the coffee was made and False otherwise"""
    if checkResources(i_coffee):
        data.resources["water"]-=data.MENU[i_coffee]["ingredients"]["water"]
        data.resources["coffee"]-=data.MENU[i_coffee]["ingredients"]["coffee"]
        data.resources["money"]+=data.MENU[i_coffee]["cost"]
        if i_coffee != "espresso":
            data.resources["milk"]-=data.MENU[i_coffee]["ingredients"]["milk"]
        return True
    else:
        return False

def checkResources(i_coffee):
    """Check if there is enough ingredients to make the coffee"""
    if data.resources["water"]-data.MENU[i_coffee]["ingredients"]["water"]>=0:
        if data.resources["coffee"]-data.MENU[i_coffee]["ingredients"]["coffee"]>=0:
            if i_coffee == "espresso":
                return True
            else:
                if data.resources["milk"]-data.MENU[i_coffee]["ingredients"]["milk"]>=0:
                    return True
    return False

def getValidInput():
    i_input=input("What would you like? (Espresso/Latte/Cappuccino):").lower()
    while i_input not in ["espresso","latte","cappuccino","report","fill","off"]:
        i_input = input("Wrong input, What would you like? (Espresso/Latte/Cappuccino):").lower()
    return i_input

def getMoney(i_coffee):
    """Asks for money from the user and return True if its enough and prints it but returns false if its not enough"""
    amount=int(input("How many quarters?"))*data.coins["quarter"]+int(input("How many dimes?"))*data.coins["dime"]+int(input("How many nickels?"))*data.coins["nickel"]+int(input("How many pennies?"))*data.coins["penny"]
    cost=data.MENU[i_coffee]["cost"]
    if amount>=cost:
        print(f"Your change is ${amount-cost:.2f}.")
        return True
    return False

def coffeeMachinefunc():
    """The machine"""
    machineOn=True
    while machineOn:
        i_input=getValidInput()
        if i_input=="off":
            break
        elif i_input=="report":
            printReport()
        elif i_input=="fill":
            fillMachine()
        else:
            cost=data.MENU[i_input]["cost"]
            print(f"The {i_input} costs ${cost:.2f}.")
            if getMoney(i_input):
                if makeCoffee(i_input):
                    print(f"Here is your {i_input}, Enjoy")
                else:
                    print(f"Were sorry, we cant make a {i_input}, Try somthing else")
            else:
                print("Not enough money, Try somthing else")



turnOn()
turnOff()