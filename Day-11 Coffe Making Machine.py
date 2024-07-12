MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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
    "water": 1500,
    "milk": 1000,
    "coffee": 250,
}


def coffe_machine(customer_need):
    global MENU
    global resources
    global customer_pay
    global balance
    #stack checking
    xy="no"
    if resources['water']>=MENU[customer_need]["ingredients"]["water"]:
        if resources['milk']>=MENU[customer_need]["ingredients"]["milk"]:
            if resources['coffee']>=MENU[customer_need]["ingredients"]["coffee"]:
                if balance==0:
                    print(f"Here is Your {customer_need}.Enjoy the Drink..!")
                elif customer_pay<MENU[customer_need]["cost"]:
                    print("Sorry that's not enough money.Money refunded.")
                    return xy
                elif balance!=0:
                    balance2=round(customer_pay-MENU[customer_need]["cost"],2)                
                    print(f"Here is {balance2} in change.")
                    print(f"Here is Your {customer_need}.Enjoy the Drink..!")         
            else:
                print("Sry we don't have enough Coffee.")
                return xy
        else:
            print("Sry we don't have enough Milk.")
            return xy
    else:
        print("Sry we don't have enough Water.")
        return xy
    

account=0
statemnet=0
while statemnet==0:
    
    item=input("What would you Like? (espresso/latte/cappuccino):")
    if item=="report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"cash:${account}")        
    elif item=="service":
        print("Sry...Machine is temporarily not functioning.")
        break
    else:
        
        print("Please insert coins.")
        q=int(input("How many Quarters:"))
        d=int(input("How many dimes:"))
        n=int(input("How many nickles:"))
        p=int(input("How many pennies:"))
        customer_pay=((0.25*q)+(0.1*d)+(0.05*n)+(0.01*p))
        balance=customer_pay-MENU["latte"]["cost"]
        a=coffe_machine(customer_need=item)
        if a!="no":
            account+=MENU[item]["cost"]
            resources["water"]=(resources["water"]-MENU[item]["ingredients"]["water"])
            resources["milk"]=(resources["milk"]-MENU[item]["ingredients"]["milk"])
            resources["coffee"]=(resources["coffee"]-MENU[item]["ingredients"]["coffee"])
        elif a=="no":
            print("Your amount is Refunded.")





        
        
        
            
        
        


















    


