

# 6. Lambda Function
# Lambda Function in Python (Quick Explanation)
# A lambda function in Python is an anonymous, one-liner function defined using the lambda keyword. It's typically used for small, simple operations and can take any number of arguments but has only one expression.

add = lambda x:x*2
print(add(2))


numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# which is divisible by 2, even numbers called
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

