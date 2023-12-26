import os
import random

def clear_screen():              # clean the screen
    os.system('cls')

def randoom_number():
    return random.randint(1,3)
    

def selection(product):       # selection the product for make the calculus and asign the price
    
    if product==1:          # conditionals
        product_name="A"
        price=270
    elif product==2:          # conditionals
        product_name="B"
        price=340
    elif product==3:        # conditionals
        product_name="C"
        price=390
    else:                   # conditionals
        print("Invalid")
        price=0
        product_name=""

    return price,product_name        # return the price of the product and name of product

def change(amount):          # function about change in the shop
    total=0
    while True:
        number=randoom_number()
        if number==1 and amount>=10 and total+10<=amount:  # conditionals
            total+=10
            print("$10")
        elif number==2 and amount>=50 and total+50<=amount:     # conditionals
            total+=50
            print("$50")
        elif number==3 and amount>=100 and total+100<=amount:  # conditionals
            total+=100
            print("$100")

        if total==amount:        # cycle breaker
            break
    return total

def product_payment(price, product_name):          # payment for the product and 
    added=0
    while True:
        print("Your product: ",product_name, "price: $", price)
        print("Added: $", added)
        print("1. $10")
        print("2. $50")
        print("3. $100")
        try:
            coin=int(input("Insert coins: "))
        except ValueError:
            print("Error: Invalid. ")
            continue

        clear_screen()
 
        if coin==1:            # conditionals
            added+=10 
        elif coin==2:          # conditionals
            added+=50
        elif coin==3:         # conditionals
            added+=100
        else:
            print("Invalid")
        
        if added==price:
            break
        elif added>price:
            amount=added-price
            change(amount)
            break
    
print("WELCOME")
print("1. PRODUCT A: $270")
print("2. PRODUCT B: $340")
print("3. PRODUCT C: $390")
try:
    product = int(input("Selection the product: "))   # avoid errors
except ValueError:
    print("Error: Invalid.")
    exit()

price,product_name=selection(product)             # call for papers
product_payment(price, product_name)

print("You have completed your purchase, thank you very much")          # final message