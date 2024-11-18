

array = [
    [1, 2, 3],  # Row 1
    [4, 5, 6],  # Row 2
    [7, 8, 9]   # Row 3
]
   # col1 col2 col-3

target_value = 8
for inner_array in array:
    for element in inner_array:
        if element == target_value:
            print("yes!")
            break
        else:
            continue