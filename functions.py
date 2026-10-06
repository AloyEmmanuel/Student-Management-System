import json

# Importing path
from pathlib import Path

# building a path
STUDENT_DB = Path(__file__).parent / "students.json"

# Grading them according to the score
def grading_system(score: int | float):
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

# Function that delete a student from memory.
def delete_student(student: str):
    # Deserializing the json file to python, and assigning it to a variable.
    with open(STUDENT_DB, "r") as file:
        students = json.load(file)

        # Checking if the student exist in memory
    for index, name in enumerate(students):
        if student == name["name"]:
            # Deleting student and returning success.
            del students[index]
            # updating the json file 
            with open(STUDENT_DB, "w") as file:
                json.dump(students, file, indent=4)
            return "Student deleted Successfully."

    # returns does not exist if the student doesn't exist in memory
    return f"{student} does not exist."


# print(delete_student("John"))