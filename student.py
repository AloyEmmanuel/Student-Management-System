# Student Result Management System

# importing my function
import functions

# importing json
import json

# Importing path
from pathlib import Path

# building a path
STUDENT_DB = Path(__file__).parent / "students.json"

# list to store students
students = []

# students should load with existing data, else, start with an empty list
try:
    with open(STUDENT_DB, "r") as file:
        students = json.load(file)
except FileNotFoundError:
    students = []

# Creating a loop to hold the whole program
while True:

    while True:
        # Collecting the student name,
        student_name = input("What is your name? \n").capitalize().strip()

        # checks if the number has a digit on it
        has_number = any(char.isdigit() for char in student_name)

        # Tells the student to enter a valid if the name has a digit, else it continues.
        if has_number == True:
            print("Enter a valid input")
        else:
            break

    # Validating the score input
    validation = True
    while True:
        while validation is True:
            try:
                # Collecting the student score
                math_score = int(input("Enter Your Math Score: \n"))

                # Validating the score to be between 1 - 100
                if math_score < 1 or math_score > 100:
                    print("Score should be between range of 1 - 100")

                # If the score is valid, the loop ends
                else:
                    validation = False
            except ValueError:
                print("Enter a valid score.")

        validation2 = True
        while True:
            while validation2 is True:
                try:
                    # Collecting the student english score
                    english_score = int(input("Enter Your English Score: \n"))

                    # Validating the score to be between 1 - 100
                    if english_score < 1 or english_score > 100:
                        print("Score should be between range of 1 - 100")

                    # If the score is valid, the loop ends
                    else:
                        validation2 = False
                except ValueError:
                    print("Enter a valid score")

            # Getting the average score by adding both scores and dividing by 2
            average_score = (math_score + english_score) / 2

            # Printing the result to the student
            print(
                f"{student_name} your grade is: {functions.grading_system(average_score)}"
            )

            break
        break

    # Appending the each student data in a dict format inside the list
    students.append(
        {
            "name": student_name,
            "math_score": math_score,
            "english_score": english_score,
        }
    )

    # writing to the students into a json file to store students data
    with open(STUDENT_DB, "w") as file:
        json.dump(students, file, indent=4)

    # Asking if there more student
    while True:
        another_student = input("Is there another student? (yes/no) ").lower().strip()

        # Ends the inner loop, and the outer loop start again for another student
        if another_student == "yes":
            break
        # Ends the inner loop, and the outer loop ends the whole program
        elif another_student == "no":
            break
        else:
            print("Please enter yes or no.")

    # Ends the program if the student enters no
    if another_student == "no":
        break
    

