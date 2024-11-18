

# Leetcode Problem-1

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


# Algorithm-1
# Eeach Element - Ask Are you non-zero elements
# If you are non-zero Elements,Then you need to swap both elements
# but according to C++ code, slow python code

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        rindex = 0
        jindex = 0
        while rindex < len(nums):
            if(nums[rindex]) != 0:
                temp = nums[rindex]
                nums[rindex] = nums[jindex]
                nums[jindex] = temp
                jindex = jindex + 1
            rindex = rindex + 1
        