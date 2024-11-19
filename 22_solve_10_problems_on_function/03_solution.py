
# 4. Function Returning Multiple Values

def get_student_infromation():
    student_name = "Alice"
    student_id = "E178191910"
    student_age = 21
    studnet_subjects = ["Math", "Physics", "Chemistry"]
    is_student_play_games = True
    return student_name,student_id
    
# [pair in c++ same to same concept used here!]
student_name, student_id = get_student_infromation()
print(student_name,student_id)