
# recursive function 
# print all subsequence which sum is equal to K(target-sum)
def helper(current_index,nums,sub_result_container,result_container,target_sum,current_sum):
    
    if current_index == len(nums):
        if target_sum == current_sum:
            for num in sub_result_container:
                print(num)
        return
    
    # take the current element 
    current_sum = current_sum + nums[current_index]
    sub_result_container.append(nums[current_index])
    helper(current_index+1,nums,sub_result_container,result_container,target_sum,current_sum)

    # not take current elements
    # exploring all possible solutions by building a solution incrementally and abandoning paths that fail to meet the criteria
    # backtracking [recursive calls]
    current_sum = current_sum - nums[current_index]
    sub_result_container.pop()
    helper(current_index+1,nums,sub_result_container,result_container,target_sum,current_sum)
    
    
nums = [1,2,1,4]
current_index = 0
target_sum = 4
current_sum = 0
result_container = []
sub_result_container = []

helper(current_index,nums,sub_result_container,result_container,target_sum,current_sum)
