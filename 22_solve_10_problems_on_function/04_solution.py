
# Leetcode-34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# solution --> 
# function to search first position of element in sorted array
def find_first_position(nums,target):
    print("first position function is envoked!")
    start_index = 0
    end_index = len(nums)
    mid_index = int(start_index + (end_index-start_index)/2)
    
    first_position_index = -1
    while(start_index <= end_index):
        if(nums[mid_index] == target):
            first_position_index = mid_index
            end_index = mid_index - 1
        elif(nums[mid_index] < target):
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
        mid_index = int(start_index + (end_index-start_index)/2)
            
    return first_position_index

# function to search last position of element in sorted array
def find_last_positoin(nums,target):
    print("second position function is envoked!")
    start_index = 0
    end_index = len(nums)
    mid_index = int(start_index + (end_index-start_index)/2)
    
    last_position_index = -1
    while(start_index <= end_index):
        if(nums[mid_index] == target):
            last_position_index = mid_index
            start_index = mid_index + 1
        elif(nums[mid_index] < target):
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
        mid_index = int(start_index + (end_index-start_index)/2)
            
    return last_position_index

def searchRange(nums,target):
    print("flow of code")
    first_position = find_first_position(nums,target)
    second_position = find_last_positoin(nums,target)
    return first_position,second_position


nums = [5,7,7,8,8,10]
target = 8

first_position, last_position = searchRange(nums,target)
print(first_position,last_position)