#######################################################################################
#### CCN Digital Production, Design & Development Level 3 College Interview Task 2 ####
#### by Harvey Washington (hjw45h@gmail.com)                                       ####
#### Python 3.9                                                                    ####
#######################################################################################

studentScores = [["Alice", 92], ["Bob", 78], ["Carol", 60]] # Hardcoded Table of Students + Scores as an Array
gradeBoundaries = {
    range(90,101) : "A", # Dictionary Entry that shows >90% is an A
    range(80,90)  : "B", # Dictionary Entry that shows 80%-89% is a B
    range(70,80)  : "C", # Dictionary Entry that shows 70%-79% is a C
    range(60,70)  : "D", # Dictionary Entry that shows 60%-69% is a D
    range(0,60)   : "F"  # Dictionary Entry that shows less than 60% is an F
}

def getGrade(student):
    score = student[1]
    for gradeRange, grade in gradeBoundaries.items(): # Gets & Iterates through the range from the dictionary, along with the grade.
        if score in gradeRange: # If the score which is provided in the "Score" parameter is in the range on the dictionary.
            student.append(grade)  # Append the Student's Grade to their element.
            print(f'\nStudent Name: {student[0]}') # Print the Student's Name (with a line break for visual prettiness, and f-strings for embedding elements (easier to manage that concatenating strings in my opinion))
            print(f'Score: {student[1]}%') # Print the Student's Score
            print(f'Grade: {student[2]}') # Print the Student's Grade

for student in studentScores: # Iterate through the main list of students
    getGrade(student) # Run the student as a parameter through my "getGrade" function.