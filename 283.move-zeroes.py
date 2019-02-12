#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (53.41%)
# Total Accepted:    412.6K
# Total Submissions: 772.2K
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#
#Psuedo Code:
#   1. Find 0
#   2. Delete the 0
#   3. Append 0s to end of list
class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        arrsize = len(nums)
        i = 0
        while i < arrsize:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                arrsize -= 1
            else:
                i+=1
        
