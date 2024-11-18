student_name = "Alice"
student_id = "E178191910"
student_age = 21
studnet_subjects = ["Math", "Physics", "Chemistry"]
is_student_play_games = True
extracurricular_activities = ["DSAlearning","learningReact","PlayingGame", "Dance","Code","communcation"]
email_address = "alice@gmail.com"
contact_number = "9118181818"

#problem-1

index = 0
while index < len(studnet_subjects):
    print(studnet_subjects[index])
    index = index + 1

# problem-2
current_index = 1
while current_index <= 10:
    print(current_index)
    if current_index == 8:
        break
    current_index = current_index + 1
    
# problem-3
next_index = 1
while next_index <= 10:
    print(next_index)
    if next_index == 8:
        continue
    next_index = next_index + 1