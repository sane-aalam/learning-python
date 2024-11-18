
number = 5
# recursion - multiple recursive calls 
def calculate_fib(number):
    if number <= 1:
        return number
    
    last = calculate_fib(number-1)
    second_last = calculate_fib(number-2)
    return last + second_last

result = calculate_fib(number)
print(result)

