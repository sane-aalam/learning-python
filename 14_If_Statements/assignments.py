
weight = input("Enter the weight ::")
unit = input("Enter the unit ::")

if unit.upper() == "L":
   converted_number_weight = int(weight)
   converted_number_weight = converted_number_weight * 0.45
   print(converted_number_weight)
   print(f"you are converted into KG.")
else:
    converted_number_weight = int(weight)
    converted_number_weight = converted_number_weight // 0.45
    print(converted_number_weight)
    print(f"you are converted into Pounds.{converted_number_weight}")
    
# / - floating number or // - int number (exact)