#1st National Bank of Browntown Online Banking Application

#customer class. assign user
class Customer():
    #This is an OBJECT. It has properties of Withdraw, Deposit, BalanceCheck
    def __init__ (self, name, balance = 100.00):
        self.name = name
        self.balance = balance
        print("Account made for", name, " Current Balance: $", balance)
#logic on withdraw deposit and balance
    def withdraw(self,amount):
        self.balance = self.balance - amount
        return self.balance
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance

    def balance(self):
        return self.balance
#welcome print
print("Welcome to the 1st National Bank of Browntown App")
print("All new customers get $100 deposited into their account for signing up!")
print()
name = input("Let's Get Started! What is your name: ")
customer = Customer(name)
#loop for crash avoiding
loop = True
#choice option
while loop == True:
    print("What would you like to do: (1) Withdraw   (2) Deposit   (3) Check Balance   (4) Close")
    choice = input("->")
    if choice == "1":
        print("How much are you withdrawing")
        amount = float(input("->"))
        customer.withdraw(amount)
        print("You have withdrawn ", amount)
        print("Your balance is", customer.balance)
    elif choice == "2":
        print("How much are you depositing")
        amount = float(input("->"))
        customer.deposit(amount)
        print("You have deposited ", amount)
        print("Your balance is", customer.balance)
    elif choice == "3":
        print("Your balance is", customer.balance)
    elif choice == "4":
        print("Have a good day. Hope to see you soon!")
        break
    #break loop if close
    else:
        print("Please pick a valid input and try again!")
        #else, repick valid number or continue loop on valid choice
    
