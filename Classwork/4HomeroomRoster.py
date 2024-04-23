#HOMEROOM ROSTER
#This program allows you to search for students on a list
#It will perform the following tasks: names, basic info, add/remove from list

#create an object called student
class Student:
    def __init__(self,name,grade,identification,locker_number,age, address):
        self.name = name
        self.grade = grade
        self.identification = identification
        self.locker_number = locker_number
        self.age = age
        self.address = address

#Create Student List Array:
list_of_homeroom_students = []

#Functions
def add_to_homeroom():
    print("What is the student's name?")
    name = input("->")

    print("What is the student's grade?")
    grade = input("->")

    print("What is the student's ID number?")
    identification = input("->")

    print("What is the student's locker number?")
    locker_number = input("->")

    print("What is the student's age?")
    age = input("->")

    print("What is the student's address?")
    address = input("->")

    new_student = Student(name, grade, identification, locker_number, age, address)
    print("New student has been created with the following information:")
    print("Name:", new_student.name)
    print("Grade:", new_student.grade)
    print("ID Number:", new_student.identification)
    print("Locker Number:", new_student.locker_number)
    print("Age:", new_student.age)
    print("Address:", new_student.address)
    list_of_homeroom_students.append(new_student)

def remove_from_homeroom(search_potato):
    print("Attempting to remove", search_potato, "from homeroom")
    for student in list_of_homeroom_students:
        if student.name == search_potato:
            list_of_homeroom_students.remove(student)
            print("Student has been removed!")

def get_number_of_students_in_homeroom():
    number_of_students = len(list_of_homeroom_students) 
    return number_of_students

def get_student_list():
    print("The students in your homeroom consist of:")
    for student in list_of_homeroom_students:
        print(student.name)

def search_student(potato):
    for student in list_of_homeroom_students:
        if student.name == potato:
            print("Student is on the list")
            return
    print("Student is not on the list")

def search_student_id(potato):
    for student in list_of_homeroom_students:
        if student.name == potato:
            print(student.identification)

def search_student_address(potato):
    for student in list_of_homeroom_students:
        if student.name == potato:
            print(student.address)


#Main Code
while True:
    print("What action would you like to perform")
    print("1: View Homeroom List")
    print("2: Add Student from Homeroom")
    print("3: Remove Student from Homeroom")
    print("4: Search for Student in Homeroom")
    print("5: Search Student ID")
    print("6: Search Student Address")
    print("7: Get Number of Homeroom Students")
    print("8: Exit Program ")

    choice = int(input("->"))
    if choice == 1:
        #list of students
        get_student_list()
    elif choice == 2:
        #add student
        add_to_homeroom()
    elif choice == 3:
        #remove student
        print("Which student would you like to remove?")
        search_potato = input("->")
        remove_from_homeroom(search_potato)
    elif choice ==4:
        #search student
        print("Which student would you like to search for?")
        remove_name = input("->")
        search_student(remove_name)
    elif choice == 5:
        #student id search
        print("Which student do you need an ID for?")
        potato = input("->")
        search_student_id(potato)
    elif choice == 6:
        print("Which student do you need an address for?")
        potato = input("->")
        search_student_address(potato)
    elif choice == 7:
        #number of students
        print("There are", get_number_of_students_in_homeroom(), "students in the homeroom list")
    elif choice == 8:
        #close
        print("Homeroom list closed. Have a good day")
        break

    else:
        print("Invalid Error! Please Try Again!")
