print("This is a grade calculator to calculate a score. First, enter how many points you earned on an assignment, then how many it was worth. You will see if you passed or failed")
x = input("")
y = input("")
print("Your grade is " + str(int(x)/ int(y)*100) + "%")
if int(x)/ int(y)*100 >= 60:
    print("You passed")
else:
    print("You failed")
