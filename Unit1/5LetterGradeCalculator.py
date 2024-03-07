print("This is a grade calculator to calculate a letter grade. First, enter how many points you earned on an assignment, then how many it was worth. You will see if you passed or failed")
x = input("")
y = input("")
if int(x)/ int(y)*100 > 89:
    z = "A"
elif int(x)/ int(y)*100 > 79:
    z = "B"
elif int(x)/ int(y)*100 > 69:
    z = "C"
elif int(x)/ int(y)*100 > 59:
    z = "D"
else:
    z = "F"
print("Your letter grade is " + z)
if int(x)/ int(y)*100 >= 60:
    print("You passed")
else:
    print("You failed")
