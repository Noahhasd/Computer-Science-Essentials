print("Welcome to the Simple Calculator")
print("This calculator subtracts two user-provided numbers. Enter your first number, then second and the math will be done")


while True:

    try:
        x = float(input("Give me a number    "))
        y = float(input("Give me another number   "))
        answer = x - y
        print(x ,"-",  y, "=", answer)
        break
    except:
        print("You did not provide a valid number! Please try again!")

