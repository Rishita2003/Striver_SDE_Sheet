'''
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
 

Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
Constraints:

1 <= nums.length <= 5 * 104
-231 <= nums[i] <= 231 - 1
'''

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergesort(low,high):
            if low>=high:
                return 0
            mid=(low+high)//2
            c=mergesort(low,mid)+mergesort(mid+1,high)
            i=low
            j=mid+1
            while i<=mid and j<=high:
                if nums[i]>2*nums[j]:
                    c+=mid-i+1
                    j+=1
                else:
                    i+=1
            nums[low:high+1]=sorted(nums[low:high+1])
            return c
        return mergesort(0,len(nums)-1)
