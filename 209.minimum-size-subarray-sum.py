#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (34.08%)
# Total Accepted:    162K
# Total Submissions: 473.6K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        right = 0
        ans = 0 
        n = len(nums)
        found = False
        while right <= n:
            #if sum(nums[left:right]) >= s:
            while sum(nums[left:right]) >= s and right - left >= 1:
                if(not found):
                    ans = right - left
                    found = True
                if(right - left < ans and found):
                    ans = right - left
                #print(nums[left:right])
                left += 1
            right +=1
        return ans
