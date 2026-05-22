""""
Q.no : 217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""


class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
        
arr1=[1,2,3,3,4]
print(Solution().containsDuplicate(arr1))
