import random

answer = -1
user_guess = -1
lives_counter = 10
loop = True

print("Welcome to the single player guessing game.")
print("Guess a number between 1-100")
answer = random.randint(1, 100)

while loop == True:
    if lives_counter <= 0:
        loop == False
        print("You have failed to guess the number. The number was", answer)
        break
    user_guess = input("")
    if float(user_guess) > answer:
        lives_counter -= 1
        print("Guess Lower. You have", lives_counter, "lives left.")
    elif float(user_guess) < answer:
        lives_counter -= 1
        print("Guess Higher. You have", lives_counter, "lives left.")
    elif float(user_guess) == answer:
        print("Congratulations! You guessed the number. The number was", answer)
        break
    else:
        print("An Error has occured")
        break
