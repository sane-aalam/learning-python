
import math

current_number = 17.4
next_number = math.ceil(current_number)
prev_number = math.floor(current_number)

print(next_number)
print(prev_number)

if current_number == prev_number and current_number == prev_number:
    print("all are eqaul!")
else:
    print("not equal")

# 1-Problem statement
# case-1 Total Number is less than 100, Number is prefect!
# case-2 Total Number is greater than 100,Number is prefect!
# case-3 Total Number is Equal to 100, Number is inValid!
total_number = current_number + next_number + prev_number
print(total_number)

if total_number < 100:
    print("Number is prefect!")
elif total_number > 100:
    print("Number is not prefect!")
else:
    print("Number is invalid!")