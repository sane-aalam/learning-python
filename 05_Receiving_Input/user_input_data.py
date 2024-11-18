
student_name = input("Enter the student Name :")
student_id = input("Enter the student Id :")
student_age = 21
studnet_subjects = ["Math", "Physics", "Chemistry"]
is_student_play_games = bool(input("Is Student Plays Game or Not ? :"))
address = {
    "street": "123 Maple Street",
    "city": "Springfield",
    "zip_code": "62704"
}
extracurricular_activities = ["DSAlearning","learningReact","PlayingGame", "Dance","Code","communcation"]
email_address = "alice@gmail.com"
contact_number = "9118181818"

print(student_age)
print(student_name)
print(is_student_play_games)

print(type(student_name))
print(type(student_age))
print(type(is_student_play_games))

# output
# 21
# Alex
# True
# <class 'str'>
# <class 'int'>
# <class 'bool'>

# same to same [0-based indexes]
first_skill = extracurricular_activities[0] 
second_skill = extracurricular_activities[1]
third_skill = extracurricular_activities[2]

print(first_skill,second_skill,third_skill)