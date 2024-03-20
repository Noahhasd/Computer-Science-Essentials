#This is an example of how to read/write a text file.
#Add this code to your VS Code, run it, and understand it
#Then, build your own code from scratch that writes and reads from a text file.

#Give your file a name. Dont forget the .txt
fileName = "business_sign_in.txt"

#create a method that writes to the text file on-demand
#content is the data that will be sent to the text file
def writeToFile(content):
    try:
        with open(fileName, 'a') as file:
            #add a '\n' to the content so it prints on a new line each time
            content = content +"\n"
            #write the content to the file
            file.write(content)
            #tell the user it was sent
            print("Welcome!")
            #close the file
            file.close()
    #in the event the file is unreachable, go here
    except:
        print("An error has occured!")

#create a method that reads from the text file on-demand
def readFromFile():
    try:
        with open(fileName, 'r') as file:
            #get the data and store it as 'content'
            content = file.read()
            #print 'content'
            print(content)
            file.close()
    except:
        print("No one has signed in yet. Try again later")

        
#Create a loop that allows the user to add content to the file, read content from the file,
#  or exit the program
while True:
    print("What would you like to do?")
    print("1: Employee Sign In   2: View Employees   3: Exit program")
    choice = input("->")
    if choice == "1":
        #Choice 1 writes to the file
        print("What is your name?")
        content = input("->")
        writeToFile(content)
        print("You have been marked as present")

    elif choice == "2":
        #choice 2 reads the content of the file
        print("Here is the list of everyone here")
        readFromFile()

    elif choice == "3":
        #choice 3 closes the program using 'break' command
        break
print("Good Bye")
