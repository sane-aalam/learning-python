
nums = [11,13,4,56,19]
target = 191

# While-loop (clean-code)
current_index = 0
while current_index < len(nums):
    if(nums[current_index] == target):
        print("YES!")
        break
    else:
        print("NO!")
        break

# creation of functon of Linear Search 
def LinearSearch(nums):
    for num in nums:
        if(num == target):
            return 1
    return 0

IsPresentOrNot = LinearSearch(nums)
print(IsPresentOrNot)