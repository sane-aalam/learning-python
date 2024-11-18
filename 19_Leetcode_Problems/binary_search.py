

class Solution(object):
    def binarysearch(self, arr,target_value):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Code Here
        start_index = 0
        end_index = len(arr) - 1
        middle_index = int(start_index + (end_index-start_index)/2)
        
        while(start_index <= end_index):
            if(arr[middle_index] == target_value):
                return middle_index
            elif(arr[middle_index] < target_value):
                start_index = middle_index + 1
            else:
                end_index = middle_index - 1
            # update the middle index
            middle_index = int(start_index + (end_index-start_index)/2)
    
        return -1

                