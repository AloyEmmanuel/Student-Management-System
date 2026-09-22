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
