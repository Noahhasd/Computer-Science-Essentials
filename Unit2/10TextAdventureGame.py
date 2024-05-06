import random

#Check Advance Variables
checks_cleared = []
purpose = ("")
win_mcnuts = "-1"
win_hairboy = "-1"
win_benny = "-1"
win_elfking = "-1"

#Guessing Game Variables
answer = -1
user_guess = -1
loop = True

#Guessing game for level 1
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

#Guessing game for level 2
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
            print('"Oh to be deafeated. You are a good lad. ADVANCE!"')
            print("You march on forward towards room three....")
            break
        else:
            print("An Error has occured")
            break

#Guessing game for level 3
def guessing_game_benny():
    global win_benny
    lives_counter = 5
    answer = random.randint(1, 25)
    print('"one through 25... go. 5 lives. "')
    print("He is soft, but stern.")
    while loop == True:
        if lives_counter <= 0:
            loop == False
            print("You have failed to guess the number. The number was", answer)
            print('"sorry. it is for your own good."')
            print("Benny slashes his weapon. It looks like a pink baseball bat.")
            print("home run. you black out...")
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
            checks_cleared.append("Benny The Chocolate Protector")
            win_benny = "1"
            print('You won against Benny. He lays tired after the battle you just had.')
            print("You march on forward towards the final room. Benny gives you a stern smile, and hands you a gallon of chocolate milk.")
            print("While of few words, you will remember his kindness")
            break
        else:
            print("An Error has occured")
            break

#Guessing game for level 4 (round logic to prevent victory)
def guessing_game_elfking():
    global win_benny
    global purpose
    lives_counter = 3
    answer = float(3.23448393832)
    print('"WE CALL HIM THE ELF KING!" Benny blurts')
    print('"HE IS FOUL! HE HAS IMPRISONED ME SINCE I WENT AND DID HIS STUPID CHALLENGE"')
    print('"YOU BROKE MY CURSE BY BEATING ME! Now, try to beat him..."')
    print("The Elf King snickers. He seems like he is not here to play nice.")
    print(player_name, ", come at me.... 3 guesses. Number 1 through 5...")
    print("He smiles. His mouth not moving. He has a strong aura though")
    print('"Telepathy.... Good luck.." Benny remains by your side')
    while loop == True:
        if lives_counter <= 0:
            loop == False
            print("You have failed to guess the number. The number was", round(int(3.4),0))
            print('You stand back astonished! Chances are you already picked 3...')
            print("He is talking to you")
            print(player_name,", are you forgetting.. about ROUND?!?!?!")
            print("You indeed did. You sense a monologue about to happen from The Elf King.")
            print("However, Benny is getting tired and throws his bat at the King")
            print("He falls 3 inches. But for a small man, that is a large height.")
            print("Moral of this story, throwing bats is way more efficient than playing a guessing game for victory..")
            exit()
        user_guess = input("->")
        if float(user_guess) > answer:
            lives_counter -= 1
            print("Guess Lower. You have", lives_counter, "lives left.")
        elif float(user_guess) < answer:
            lives_counter -= 1
            print("Guess Higher. You have", lives_counter, "lives left.")
        else:
            print("An Error has occured")
            break

#Transport to level 1
def level_one():
    print("You enter your first gate. The door is unlocked as it is the first goal to overcome...")
    print("Glancing, you see no human. Rather, a tree with acorns. And a hungry squirrel draws near")
    print("MR. MCNUTS SEEKS HIS REVENGE!")
    guessing_game_mcnuts()

#Transport to level 2 (level 1 logic finish) 
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

#Transport to level 3 (level 2 logic finish)         
def level_three():
    if win_hairboy == ("1"):
        print('You walk into the 3rd room. You feel a heavy aura draw upon you. You tremble')
        print('A softspoken man emerges. He is very tall and intimdating. But, he seems kind somehow')
        print('Under his breath, he says his name..... Benny. He draws, ready to fight.')
        guessing_game_benny()
    elif win_hairboy == ("-1"):
        print("Challenger 2 has not been defeated yet. Please take on Challenger 2 first")
    else:
        print("An Error has occured")

#Transport to level 4 (level 3 logic finish) 
def final_battle():
    global purpose
    if win_benny == ("1"):
        print('The 4th and final room appears. You enter. You see Benny trailing behind...')
        print("You feel as if he knows something you do not. You question why you are here.")
        print("You knoow you want to be the master guesser, but why?")
        print("What is your purpose...")  
        purpose = input("->")
        print(purpose,"?..... wise.")
        print("You hear a crash and feel a presence")
        print('"WELCOME TO BROWN TOWN!')
        guessing_game_elfking()

    elif win_hairboy == ("-1"):
        print("Challenger 3 has not been defeated yet. Please take on Challenger 2 first")
    else:
        print("An Error has occured")

#Game Introduction
print("Welcome to the Master Guessing Game!")
print("You are on the quest to be the very best at getting lucky!")
print("You will fight your way through a gauntlet of 4 expert guessers to try to crown yourself the greatest guesser of all time")
print("One wrong move and your game is over.... Enter if you dare")
print("Enter Your name, challenger.....")
player_name = input("->")

#main menu
while True:
    print("Hello,", player_name)
    print("What would you like to do? Remember, you must challange the stages in order and cannot skip ahead!")
    print("1) Challenger One")
    print("2) Challenger Two")
    print("3) Challenger Three")
    print("4) The Final Battle....")
    print("5) View Previous Wins")
    print("6) Exit")
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

    else:
        print("WHAT PART ABOUT A NUMBER 1 THROUGH 5 IS SO HARD TO COMPREHEND!?!?!?!")
