# Problem-1
# if current_temperature_weather is greater than 30
#    it's a hot day
# otherwise if it's less than 10
#    it's a cold day
# otherwise 
#    it's neither hot nor cold!

user_input = input("Enter the current temperature weather :: ")
current_temperature_weather = int(user_input)

if current_temperature_weather > 30:
    print("it's a hot day")
    take_water = "ready"
    if take_water == "ready":
        print("Drink Water!")
    else:
        print("Not Drink Water!")
elif current_temperature_weather < 10:
    print("it's a cold day")
    take_tea = "ready"
    if take_tea == "ready":
        print("you are ready to take the tea!")
else:
    print("it's neither hot nor cold!")
