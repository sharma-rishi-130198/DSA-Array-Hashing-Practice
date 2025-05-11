"""
Problem: 49. Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/description/
Difficulty: Medium

Description:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time Complexity = O(n * k log k), Space Complexity = O(n * k),
        where n is the number of strings and k is the average length of each string.

        Approach:
            - Use a hash map to store the grouped anagrams, using sorted string as the key.
            - For each string, sort it and use it as a key in the hash map to group anagrams together.
            - If the sorted string is already a key, append the current string.
            - Otherwise, create a new entry in the hash map for the sorted string.
        """
        # Using a hash map to store the grouped anagrams
        groupings_dict = {}

        # Iterate through each string in the input list
        for string in strs:
            # Sort the string and use it as a key to group anagrams
            sorted_string = str(sorted(string))  # Sort the string to generate a key

            # If the sorted string is already a key, append the current string
            if sorted_string in groupings_dict:
                groupings_dict[sorted_string].append(string)
            else:
                # Otherwise, create a new group for this key
                groupings_dict[sorted_string] = [string]

        # Extracting the grouped anagrams into a result list
        result = []
        for grouping in groupings_dict.values():
            result.append(grouping)

        return result


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(strs))
    # Output: [["eat","tea","ate"],["tan","nat"],["bat"]]