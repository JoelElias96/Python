from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu=Menu()
maker=CoffeeMaker()
money=MoneyMachine()
run=True
while run:
    i_input=input(f"Please enter what would you like to make: {menu.get_items()}").lower()
    if i_input=="off":
        run=False
    elif i_input=="report":
        maker.report()
        money.report()
    else:
        mycoffee=menu.find_drink(i_input)
        if mycoffee:
            if maker.is_resource_sufficient(mycoffee):
                if money.make_payment(mycoffee.cost):
                    maker.make_coffee(mycoffee)







