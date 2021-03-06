"""

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements 
without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence 
of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104

Difficulty: Medium
Completed: 5/29/2022

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

"""
Explanation:

We use a dp array that is initialized at 1 for every index. Then we 
calculate each index by finding if there are any values before it that
are smaller than the value at index i. If so, then we make dp[i] the
maximum between its previous value and dp[j] + 1 where j is the index of
the value where nums[j] < nums[i]. In the end, we return the maxiumum
value of our dp matrix.

Time Complexity: O(N^2)
Space Complexity: O(N)
"""
