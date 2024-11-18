
netfix_collection = ["Learning DSA","Money Heist Season 1","Money Heist Season 2","Money Heist Season 3", "Learing Python for beginners", "Python for web development"]

# taking user input 
user_searching_thing = input("Enter the search data:")
print(user_searching_thing)
print(type(user_searching_thing))

current_index = 0;
while current_index < len(netfix_collection):
    if netfix_collection[current_index] == user_searching_thing:
        print("This series is present into the our collection!")
        break;
    elif netfix_collection[current_index] == user_searching_thing and netfix_collection[current_index] == user_searching_thing:
        print("This is learning collection!") 
        break
    else:
        print("This series is not present into the our colelction!")
        continue
    current_index  = current_index + 1
        
        