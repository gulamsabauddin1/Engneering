# Brute Force
# def solution(nums,target):
#     sum=0
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             sum=nums[i]+nums[j]
#             if sum==target:
#                 return [index for index in (i,j)]
    
#Dictonary
def solution(nums, target):
        seen = {}
        for i in range(len(nums)):
            current_num = nums[i]
            complement = target - current_num
            if complement in seen:
                return [seen[complement], i]
            seen[current_num] = i  
    
    
nums=[2,7,11,15]    
target=17
print(solution(nums,target))