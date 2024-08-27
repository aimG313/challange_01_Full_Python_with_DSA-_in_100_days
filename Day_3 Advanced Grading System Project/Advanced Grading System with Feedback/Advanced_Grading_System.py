# Input the mark
mark = int(input("Enter your mark: "))

# Validate the mark
if mark < 0 or mark > 100:
    print("Invalid mark! Please enter a value between 0 and 100.")
else:
    # Determine the grade
    if mark >= 91:
        grade = "A+"
        feedback = "Excellent work! Keep it up!"
    elif mark >= 81:
        grade = "A"
        feedback = "Great job! You're doing very well."
    elif mark >= 71:
        grade = "B"
        feedback = "Good effort! A little more focus will take you to the top."
    elif mark >= 61:
        grade = "C"
        feedback = "Fair performance. Try to work on your weak areas."
    elif mark >= 50:
        grade = "D"
        feedback = "You passed, but there's room for improvement."
    else:
        grade = "F"
        feedback = "You failed. Don't get discouraged; work harder next time."

    # Output the grade and feedback
    print("Your grade:",grade)
    print("Feedback:",feedback)
