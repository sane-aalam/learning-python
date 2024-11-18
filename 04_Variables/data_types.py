
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

print(type(student_age))
print(type(student_name))
print(type(is_student_play_games))
print(type(extracurricular_activities))
print(type(address))

# output -> <class "int"> we will explore more depth,means type-int,str,bool,list,dic
# <class 'int'>
# <class 'str'>
# <class 'bool'>
# <class 'list'>
# <class 'dict'>

if type(student_age) == type(contact_number):
    print("both types are equal")
else:
    print("both types are not equal!")
