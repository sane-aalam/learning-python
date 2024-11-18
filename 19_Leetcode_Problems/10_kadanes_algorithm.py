

def maxSubArray(arr):
    current_sum = 0
    maximum_sum = -99999999
    for num in arr:
        current_sum = current_sum + num
        if current_sum > maximum_sum:
            maximum_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    
    return maximum_sum

arr = [2, 3, -8, 7, -1, 2, 3]
result = maxSubArray(arr)
print(result)
# The subarray {7, -1, 2, 3} has the largest sum 11.