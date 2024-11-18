

class Solution(object):
    def binarysearch(self, nums,target):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start_index = 0
        end_index = len(nums) - 1
        middle_index = start_index + (end_index-start_index)/2
        
        while(start_index <= end_index):
            if(nums[middle_index] == target):
                return middle_index
            elif(nums[middle_index] < target):
                start_index = middle_index + 1
            else:
                end_index = middle_index - 1
            # update the middle index
            middle_index = start_index + (end_index-start_index)/2
    
        return -1
                