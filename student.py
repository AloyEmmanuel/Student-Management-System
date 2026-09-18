# Student Result Management System

# Creating a boolean to keep the while loop running
while True:
    # Collecting the student name

    student_name = input("What is your name? \n").capitalize().strip()

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

            # Getting the total score by adding scores
            total_score = (math_score + english_score) / 2

            # Grading them according to the score
            def grading_system(score):
                if score <= 39:
                    return "F"
                elif score >= 40 and score < 45:
                    return "E"
                elif score >= 45 and score < 50:
                    return "D"
                elif score >= 50 and score < 60:
                    return "C"
                elif score >= 60 and score < 70:
                    return "B"
                else:
                    return "A"

            # Printing the result to the student
            print(f"{student_name} your grade is: {grading_system(total_score)}")
            another_student = input("Do you want to continue? ").lower()
            if another_student == "no":
                break
