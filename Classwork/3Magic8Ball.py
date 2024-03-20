import random
response = random.randint(1, 8)

print("Welcome to the Magic 8 Ball\nAsk the Magic 8 Ball a Question")
question = input("") 
print("You asked,", question)
print("The Magic 8 Ball responds with:")
if response == 1:
    print("Ask again later")
elif response == 2:
    print("Uh, ok")
elif response == 3:
    print("Sir yes ma'am")
elif response == 4:
    print("IDK. Figure it out")
elif response == 5:
    print("OH HECK NO")
elif response == 6:
    print("Ask the elf reading this right now")
elif response == 7:
    print("Sure")
elif response == 8:
    print("No.")
else:
    print("Oopsies we made a mistake")
