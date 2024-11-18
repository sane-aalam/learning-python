
number_collection = [11,12,13,14]

sum_even = 0
sum_odd = 0

for num in number_collection:
    if num % 2 == 0:
        sum_even = sum_even + num
    else:
        sum_odd = sum_odd + num
        
print(sum_odd)
print(sum_even)