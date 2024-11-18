
# -> Meaningful variable names
# 1. Use Descriptive Names
# 2. Use Snake Case for Multi-Word Names ex- (full_name)
# 3. Avoid Generic Names
# 4. Prefix with Context When Necessary
# 5. Use Plural Form for Lists or Collections
# 6. Good Variable Names helps to understand codebase

student_name = "Alice"
student_id = "E178191910"
student_age = 21
studnet_subjects = ["Math", "Physics", "Chemistry"]
is_student_play_games = True
# Javascript(key value of pair)
address = {
    "street": "123 Maple Street",
    "city": "Springfield",
    "zip_code": "62704"
}
extracurricular_activities = ["DSAlearning","learningReact","PlayingGame", "Dance","Code","communcation"]
email_address = "alice@gmail.com"
contact_number = "9118181818"


# print the data of students 
print(student_name)
print(student_id)
print(student_age)
print(studnet_subjects)
print(is_student_play_games == True)
print(address)
print(extracurricular_activities)
print(email_address)
print(contact_number)

#for loop in python(clean)
for skill in extracurricular_activities:
    print(skill)
 
"""
-> Working (depth understanding in C++)

for(int currentIndex = 0 currentIndex < extracurricular_activities.size(); currentIndex++){
    cout << extracurricular_activities[currentIndex] << ""
}

1. Ease of Learning and Syntax Simplicity
2. short code 
3. clean code
4. Rapid Development and Prototyping
5. Memory Management and Safety
6. Applications in Data Science, AI, and Machine Learning
7. Career and Job Market
8. fun to learn python
"""

if extracurricular_activities[4] == "Dance":
    print("data is correct")
else:
    print("data is not correct!")
    