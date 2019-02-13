#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (19.59%)
# Total Accepted:    42.7K
# Total Submissions: 218.2K
# Testcase Example:  '[4,2,3]'
#
# Given an array with n integers, your task is to check if it could become
# non-decreasing by modifying at most 1 element.
# 
# We define an array is non-decreasing if array[i]  holds for every i (1 
# 
# Example 1:
# 
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
# 
# 
# 
# Example 2:
# 
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
# 
# 
# 
# Note:
# The n belongs to [1, 10,000].
# 
# None decreasting: does constant count as non decreasing?
# None decreasing:
#   1. nums[i] <= nums[i+1]
# Logic:
# Iter through the list, find decreasing item and modify it to make it non decreasing
# Set a counter or flag and set that to true after the first item has been modified
# 
# Edge Case:
# Nothing to compare to, list only has 1 element
# 3,4,2,3

class Solution:
    def checkPossibility(self, nums: 'List[int]') -> 'bool':
        p = None
        #if len(nums) <= 2:
        #    return True
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]: 
                if p is not None:
                    return False
                p = i
        return (p is None or p == 0 or p == len(nums)-2 or
                nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2])
