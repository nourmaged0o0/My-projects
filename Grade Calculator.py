def problem1():

    def calculate_again():#to make the user choose if he calculate again or exit the program
        user_choice = input("A) Calculate a new grade\nB) Exit\n").upper()
        while user_choice !="A" and user_choice!="B": #to validate the choice
            user_choice = input("invalid choice\nA) Calculate new grade\nB) Exit\n").upper()
        if user_choice =="A": #to restart the program if user choose this option
            grade_calculator()
        else:
            exit()

    def grade_calculator():
        while True:
            try: #to make sure that user enter a float value
                mark = float(input("Enter your mark: "))
                while mark <0 or mark >100: #choose the range where mark should be
                    mark = float(input("invalid number\nPlease enter your mark: "))
                break
            except ValueError: #runs when user enter a not intger value
                print("invalid number")
        if mark >= 96:
            print("Your grade is A+")
        elif mark <96 and mark >=92.5:
            print("Your grade is A")
        elif mark <92.5 and mark >=90:
            print("Your grade is A-")
        elif mark <90 and mark >=87.5:
            print("Your grade is B+")
        elif mark <87.5 and mark >=82.5:
            print("Your grade is B")
        elif mark <82.5 and mark >=80:
            print("Your grade is B-")
        elif mark <80 and mark >=77.5:
            print("Your grade is C+")
        elif mark <77.5 and mark >=72.5:
            print("Your grade is C")
        elif mark <72.5 and mark >=70:
            print("Your grade is C-")
        elif mark <70 and mark >=67.5:
            print("Your grade is D+")
        elif mark <67.5 and mark >=62.5:
            print("Your grade is D")
        elif mark <62.5 and mark >=60:
            print("Your grade is D-")
        elif mark <60:
            print("Your grade is F")
        calculate_again()

    print("*** Welcome to our grade calculator ***")#welcome message
    grade_calculator()
