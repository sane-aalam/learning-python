
# *
# **
# ***
# ****

# wrong way to write code
num = 4
outter_index = 1
while outter_index <= num:
    inner_index = 1
    while inner_index <= outter_index:
        print("*")
        inner_index = inner_index + 1
    outter_index = outter_index + 1
    

# right way to write code 
num = 4
outter_index = 1
while outter_index <= num:
    inner_index = 1
    while inner_index <= outter_index:
        print("*", end="")  # Print * without moving to the next line
        inner_index += 1
    print()  # Move to the next line after each row
    outter_index += 1

