import random

checks_cleared = []

#Guessing Game Variables
answer = -1
user_guess = -1
loop = True

def guessing_game_mcnuts():
    lives_counter = 7
    answer = random.randint(1, 20)
    print("Mr. McNuts makes barley audible rodent noises.")
    print("For the sake of simplicity, his nonsense translates to 7 lives with a number 1-20")
    print("He wishes you pain.... make your first guess.....")
    while loop == True:
        if lives_counter <= 0:
            loop == False
            print("You have failed to guess the number. The number was", answer)
            print("You lay defeated. As Mr. McNuts feasts on your corpse. He wishes it was covered in peanut butter...")
            print("You do not taste very good....")
            exit()
        user_guess = input("->")
        if float(user_guess) > answer:
            lives_counter -= 1
            print("Guess Lower. You have", lives_counter, "lives left.")
        elif float(user_guess) < answer:
            lives_counter -= 1
            print("Guess Higher. You have", lives_counter, "lives left.")
        elif float(user_guess) == answer:
            print("Congratulations! You guessed the number. The number was", answer)
            checks_cleared.append("check_one")
        else:
            print("An Error has occured")
            break


def level_one():
    print("You enter your first gate. The door is unlocked as it is the first goal to overcome...")
    print("Glancing, you see no human. Rather, a tree with acorns. And a hungry squirrel draws near")
    print("MR. MCNUTS SEEKS HIS REVENGE!")
    guessing_game_mcnuts()
    
def level_two():
    pass

def level_three():
    pass

def final_battle():
    pass

#Game Introduction
print("Welcome to the Master Guessing Game!")
print("You are on the quest to be the very best at getting lucky!")
print("You will fight your way through a gauntlet of 4 expert guessers to try to crown yourself the greatest guesser of all time")
print("One wrong move and your game is over.... Enter if you dare")
print("Enter Your name, challenger.....")
player_name = input("->")

while True:
    print("Hello,", player_name)
    print("What would you like to do? Remember, you must challange the stages in order and cannot skip ahead!")
    print("1) Challenger One")
    print("2) Challenger Two")
    print("3) Challenger Three")
    print("4) The Final Battle....")
    print("5) Exit")
    option_input = input("->")

    if option_input == "1":
        level_one()
    elif option_input == "2":
        level_two()
    elif option_input == "3":
        level_three()
    elif option_input == "4":
        final_battle()
    elif option_input == "5":
        print("Are you sure you want to quit now? You will lose EVERYTHING! (yes/no)")
        leave = input("->")
        if leave == "yes":
            print("womp. womp.")
            break
        elif leave == "no":
            print("GOOD LAD! KEEP FIGHTING ON!")
        else:
            print("If you are seeing this, you either cannot read, hit the caps button, or have the spelling of a 2nd grader!")
            print("maybe it is your sign to give up after all....")
    else:
        print("WHAT PART ABOUT A NUMBER 1 THROUGH 5 IS SO HARD TO COMPREHEND!?!?!?!")



            
        

    
