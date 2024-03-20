#VARIABLES
orderComplete = False
totalCost = 0
#WELCOME THE USER TO THE POINT OF SALE(POS)
print()
print()
print("Welcome to the Browntown Burger Joint, voted 2nd best Burger in Browntown")
print()

#ASK THEM FOR THEIR NAME AND STORE IT IN name
name = input("Can I have your name please?  ")
print()
print("Thanks " + name)
print()
print()

#POINT OF SALE LOOP
while orderComplete == False:
    #STAY IN THIS LOOP UNTIL THEY SELECT "COMPLETE ORDER"
    print()
    print ("What would you like to order: Burgers, Sides, Drinks, Complete Order.")
    menu = input("-> ")
    
    
    if menu == "Burgers":
        #IF THEY WANT TO ADD A BURGER:
        print("We offer the following burgers:")
        print("1: Hamburger $5.50")
        print("2: Cheesebuger $6.00")
        print("3: Western burger (Cheese, onion, western sauce) $6.75")
        print("4: Beefy Burger (A large burger) $10.50")
        burgerChoice = input("What would you like (input a number 1-4): ")
        #BURGER 1: HAMBURGER
        if burgerChoice == "1":
            totalCost = totalCost + 5.50
            print("You added Hamburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 2: CHEESEBURGER
        elif burgerChoice == "2":
            totalCost = totalCost + 6.00
            print("You added Cheeseburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 3: WESTERN BURGER
        elif burgerChoice == "3":
            totalCost = totalCost+ 6.75
            print("You added Western Burger to your order")
            print("Your total cost so far: $", totalCost)
        
        #BURGER 4: ADD ONE HERE
            #ADD A NEW BURGER OPTION AND UPDATE ALL CODE ABOVE TO MAKE IT WORK
        elif burgerChoice == "4":
            totalCost = totalCost+ 10.50
            print("You added Beefy Burger to your order")
            print("Your total cost so far: $", totalCost)


            
        #IF THEY GET HERE, THEY DID NOT MAKE A VALID SELECTION
        else:
            print("please make a valid choice")
        
    elif menu == "Sides":
        print("sides")
        print("We offer the following Sides:")
        print("1: Loaded Fries $5.50")
        print("2: Epic Potato $6.00")
        print("3: Golden Glazed Mozzerella Stix $6.75")
        sideChoice = input("What would you like (input a number 1-3): ")
           
        if sideChoice == "1":
            totalCost = totalCost + 5.50
            print("You added Loaded Fries to your order")
            print("Your total cost so far: $", totalCost)
        elif sideChoice == "2":
            totalCost = totalCost + 6.00
            print("You added Epic Potato to your order")
            print("Your total cost so far: $", totalCost)
        elif sideChoice == "3":
            totalCost = totalCost+ 6.75
            print("You added Golden Glazzed Mozzerela Stix to your order")
            print("Your total cost so far: $", totalCost)
        else:
            print("please make a valid choice")
    
        
    elif menu == "Drinks":
        print("drinks")
        print("We offer the following Drinks:")
        print("1: Water $1.00")
        print("2: Milk $1.50")
        print("3: THE SUPREME MILK OF CHOCOLATE $3.50")
        drinkChoice = input("What would you like (input a number 1-3): ")
           
        if drinkChoice == "1":
            totalCost = totalCost + 1
            print("You added Water to your order")
            print("Your total cost so far: $", totalCost)
        elif drinkChoice == "2":
            totalCost = totalCost + 1.50
            print("You added Milk to your order")
            print("Your total cost so far: $", totalCost)
        elif drinkChoice == "3":
            totalCost = totalCost+ 3.50
            print("You added THE SUPREME CHOCOLATE MILK to your order")
            print("Your total cost so far: $", totalCost)
        else:
            print("please make a valid choice")
        
    
    elif menu == "Complete Order":
        #IF THEY SELECT COMPLETE ORDER, SET THE ORDERCOMPLETE TO TRUE
        orderComplete = True
        print()

        #GIVE THEM THEIR TOTALS
        print("Order finished, " + name)
        print("You have ordered the burger, side and drink options of:", str(burgerChoice) + str(sideChoice) + str(drinkChoice))
        print("Subtotal: $", totalCost)
        totalTax = float(totalCost) * 0.06
        print("Tax: $", (totalTax))
        grandTotal = print("Grand Total: $", float(totalCost) + float(totalTax))
 
        
    else:
        print("Sorry, not a valid choice, please start over...")

#THE USER ONLY GETS HERE IF THEY FINISH THEIR ORDER
print("Thank you for eating with us!")
