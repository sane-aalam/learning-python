
numbers = [1,-2,4,5,6,-8,-9,10,-1110]

count_postive_number = 0
count_negative_number = 0
for num in numbers:
    if num > 0:
        count_postive_number = count_postive_number + 1
    else:
        count_negative_number = count_negative_number + 1

print(f"TotalNumber of Positive Elements {count_postive_number}")
print(f"TotalNumber of Negative Elements {count_negative_number}")