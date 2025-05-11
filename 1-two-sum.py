"""
Problem: 1. Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""

from typing import List

class Solution:
    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
        """
        Time Complexity = O(n^2), Space Complexity = O(1)
        Approach:
            - Run 2 nested loops and try all combinations of pairs to identify if their sum equals target.
        """
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]

    def twoSum_optimal(self, nums: List[int], target: int) -> List[int]:
        """
        Time Complexity = O(n), Space Complexity = O(n)
        Approach:
            - Use a hash map to store seen numbers and their indices.
            - For each number, calculate the difference (target - num).
            - If the difference is already in the map, return the stored index and current index.
        """
        num_map = {}  # value -> index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [num_map[diff], i]
            num_map[num] = i
        return [-1, -1]


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9

    print("Brute Force:", sol.twoSum_brute_force(nums, target))   # Output: [0, 1]
    print("Optimal:", sol.twoSum_optimal(nums, target))           # Output: [0, 1]