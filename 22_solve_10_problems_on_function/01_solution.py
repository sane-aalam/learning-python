
# def square_finder(num):
#     sequre_value = num * num
#     return sequre_value

def square_finder(num):
    sequre_value = num ** 2
    return sequre_value

num = int(input("Enter the number --> "))
square_value = square_finder(num)
print(square_value)