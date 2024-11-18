
student_name = "Alice"
student_id = "E178191910"
email_address = "alice@gmail.com"
contact_number = "9118181818"
course_name = "Python for beginners"
teacher_name = "VivakShram"
principle_name = "vkverma"

lower_case_string = student_name.upper()
uppper_case_string = student_name.lower()

print("hello world".capitalize())  # "Hello world"
# str.casefold()
# Returns a lowercase version of the string, more aggressive than lower()
teacher_information = "DBMS"
print(teacher_information.casefold())
print("HELLO".lower())  # "hello"
print("hello".upper())
print("Hello".swapcase())
print("hello world this".title())

# Alignment Methods
# str = "methods"
# str.center()
# str.just()

# Search and Query Methods

# student_name.startswith() -> start to present or not
# student_name.endswith()  --> end to present or not 
# student_name.find()  --> Returns the lowest index of the substring
# student_name.rfind() --> Returns the highest index of the substring
# student_name.index() 
# student_name.count()
# student_name.rindex()

given_string = "Hello world!"
present_or_not_solution1 = given_string.startswith("H")
present_or_not_solution2 = given_string.startswith("He")
present_or_not_solution3 = given_string.startswith("Hell")
present_or_not_solution4 = given_string.startswith("hellysirt")

print(present_or_not_solution1)
print(present_or_not_solution2)
print(present_or_not_solution3)
print(present_or_not_solution4)

print(given_string.find("Hel"))
print(given_string.rfind("w"))
print(given_string.count("l"))


#  Query Methods
print("abc123".isalnum())
print("abc".isalpha())
print("123".isdigit())  
print("abc".islower())  # True
print("ABC".isupper())  # True
print("   ".isspace())  # True


