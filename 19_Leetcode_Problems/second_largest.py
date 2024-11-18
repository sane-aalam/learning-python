

#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        first_largest_element = -1
        second_largest_element = -1
        for num in arr:
            if num > first_largest_element:
                second_largest_element = first_largest_element
                first_largest_element = second_largest_element
            elif num < first_largest_element and num > second_largest_element:
                second_largest_element = num
        
        return second_largest_element