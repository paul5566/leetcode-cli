#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#
# https://leetcode.com/problems/first-bad-version/description/
#
# algorithms
# Easy (28.64%)
# Total Accepted:    199K
# Total Submissions: 694.1K
# Testcase Example:  '5\n4'
#
# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the quality
# check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.
# 
# You are given an API bool isBadVersion(version) which will return whether
# version is bad. Implement a function to find the first bad version. You
# should minimize the number of calls to the API.
# 
# Example:
# 
# 
# Given n = 5, and version = 4 is the first bad version.
# 
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# 
# Then 4 is the first bad version. 
# 
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
#
# Thoughts:
# Implement a sort of a Binary Search
# Naive way: iterate from n to 0
#   Base condition: isBadVersion == True
#   Need to find both last good version and first bad version
# Edge Cases:
# 1. All versions are bad
# 2. Only 1 version

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        while(high - low != 1):
            #print(high, low)
            mid = int((low+high)/2)
            if isBadVersion(mid) == True:
                high = mid
            if isBadVersion(mid) == False:
                low = mid
        return high