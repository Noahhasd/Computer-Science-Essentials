print("Welcome to the Complex Calculator")
print("This project will combine all calculators into one. Enter a number and you will get a confirmation on what math operation is engaged. 1=Add, 2=Subtract, 3=Multiply, 4=Divide")
user_put = input()
if user_put == "1":
    print("This calculator adds two user-provided numbers. Enter your first number, then second and the math will be done")
    x = input("")
    print("+")
    y = input("")
    print("=" +  str(int(x) + int(y)))
elif user_put == "2":
    print("This calculator subtracts two user-provided numbers. Enter your first number, then second and the math will be done")
    x = input("")
    print("-")
    y = input("")
    print("=" +  str(int(x) - int(y)))
elif user_put == "3":
    print("This calculator multiplies two user-provided numbers. Enter your first number, then second and the math will be done")
    x = input("")
    print("x")
    y = input("")
    print("=" +  str(int(x) * int(y)))
elif user_put == "4":
    print("This calculator divides two user-provided numbers. Enter your first number, then second and the math will be done")
    x = input("")
    print("/")
    y = input("")
    print("=" +  str(int(x) / int(y)))
else:
    print("A NUMBER 1 THROUGH 4 DUMMY!!!")
