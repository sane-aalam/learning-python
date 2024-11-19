
# short-way to write the code
# *args to handle arguments of the function 
# *easy to undersand way 
def sum_all_numbers(*args):
    print(*args)
    return sum(*args)

nums = [5,7,7,8,8,10]
result_value = sum_all_numbers(nums)
print(result_value)

# [] = list 
# () = tuple 