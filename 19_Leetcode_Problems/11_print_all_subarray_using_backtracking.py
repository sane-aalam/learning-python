

def helper(current_index,nums,sub_result_container,result_container):
    
    if current_index == len(nums):
        for num in sub_result_container:
            print(num)
        # store all subsequence into the 2D-container
        result_container.append(sub_result_container)
        return
    
    # take the current element 
    sub_result_container.append(nums[current_index])
    helper(current_index+1,nums,sub_result_container,result_container)

    # not take current elements
    # exploring all possible solutions by building a solution incrementally and abandoning paths that fail to meet the criteria
    # backtracking [recursive calls]
    
    sub_result_container.pop()
    helper(current_index+1,nums,sub_result_container,result_container)
    
    
nums = [2,1,3]
current_index = 0
result_container = []
sub_result_container = []

helper(current_index,nums,sub_result_container,result_container)
