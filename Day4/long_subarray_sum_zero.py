'''
Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

Example 1:

Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.
Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 105
-1000 <= A[i] <= 1000, for each valid i
'''

from math import *
from collections import *
from sys import *
from os import *

def LongestSubsetWithZeroSum(arr):
    m=0
    for i in range(len(arr)):
        s=0
        for j in range(i,len(arr)):
            s+=arr[j]
            if s==0:
                m=max(m,j-i+1)
    return m

    pass
