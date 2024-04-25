import random

#Check Advance Variables
checks_cleared = []
win_mcnuts = "-1"
win_hairboy = "-1"


#Guessing Game Variables
answer = -1
user_guess = -1
loop = True

def guessing_game_mcnuts():
    global win_mcnuts
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
            checks_cleared.append("Mr. McNuts")
            win_mcnuts = "1"
            print("Mr. McNuts got very angry after your victory. He lunged at you with his crooked buck-teeth trying to attack!")
            print("Suddenly, a long strand of majestic dirty blonde hair flows from the crack in the next room over")
            print("The magnificant hair lassos McNuts and immobalizes him. You wonder what it is about and march on forward....")
            break
        else:
            print("An Error has occured")
            break

def guessing_game_hairboy():
    global win_hairboy
    lives_counter = 5
    answer = random.randint(1, 20)
    print('"A NUMBER 1 THROUGH 20! 5 LIVES! OUR BATTLE WILL BE LEGENDARY!!!"')
    while loop == True:
        if lives_counter <= 0:
            loop == False
            print("You have failed to guess the number. The number was", answer)
            print('"You put up a good fight... Unfortunatly your road ends here. Take some hair spray for the road"')
            print("The travel size bag of hair spray was thrown to you. While Hair Boy was kind, you cannot help but feel insulted somehow...")
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
            checks_cleared.append("Gorgeous Hair Boy")
            win_hairboy = "1"
            break
        else:
            print("An Error has occured")
            break

def level_one():
    print("You enter your first gate. The door is unlocked as it is the first goal to overcome...")
    print("Glancing, you see no human. Rather, a tree with acorns. And a hungry squirrel draws near")
    print("MR. MCNUTS SEEKS HIS REVENGE!")
    guessing_game_mcnuts()
    
def level_two():
    if win_mcnuts == ("1"):
        print("Uneasy of the strands of hair that just flew from the room, you continue onto the second room")
        print('"Hello, my name is Gorgeous Hair Boy," a voice reaches out to you')   
        print('"That squirrel is a little bit of a nut job. If you lose, I will not kill you"')
        print('"I joined the Master Guesser Gauntlet for thrills, and for someone who can test my skills"')
        guessing_game_hairboy()
    elif win_mcnuts == ("-1"):
        print("Challenger 1 has not been defeated yet. Please take on Challenger 1 first")
    else:
        print("An Error has occured")
        
def level_three():
    if win_hairboy == ("1"):
        print('Advancement Text')
    elif win_hairboy == ("-1"):
        print("Challenger 2 has not been defeated yet. Please take on Challenger 2 first")
    else:
        print("An Error has occured")

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
    print("5) View Previous Wins")
    print("6) Exit")
    print("7) DEBUG: DELETE AFTER GAME IS DONE")
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
        print("Here is all of your previous wins.")
        print("Opponets listed several times have been defeated several times")
        print(checks_cleared)
    elif option_input == "6":
        print("Are you sure you want to quit now? You will lose EVERYTHING! (yes/no)")
        leave = input("->")
        if leave == "yes":
            print("womp. womp.")
            exit()
        elif leave == "no":
            print("GOOD LAD! KEEP FIGHTING ON!")
        else:
            print("If you are seeing this, you either cannot read, hit the caps button, or have the spelling of a 2nd grader!")
            print("maybe it is your sign to give up after all....")
    elif option_input == "7":
        print("DEBUG. ENTER FIGHT YOU WANT TO SKIP TO")
        debug = input("->")
        if debug == "1":
            guessing_game_mcnuts()
        elif debug == "2":
            guessing_game_hairboy()
        elif debug == "3":
            pass
        else:
            pass

    else:
        print("WHAT PART ABOUT A NUMBER 1 THROUGH 5 IS SO HARD TO COMPREHEND!?!?!?!")



            
        

    
