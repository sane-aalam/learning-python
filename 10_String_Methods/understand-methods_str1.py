

user_input_first = input("Enter the first str")
user_input_second = input("Enter the second str")

if user_input_first == user_input_second.lower():
    print("both are equal")
else:
    print("both are not equal!")
    convert_upper_letter1 = user_input_first.capitalize()
    convert_upper_letter2 = user_input_second.capitalize()
    print(convert_upper_letter1)
    print(convert_upper_letter2)