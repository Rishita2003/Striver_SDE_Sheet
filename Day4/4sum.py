'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        n=len(arr)
        arr.sort()
        ans=[]
        for i in range(0,n):
            if(i>0 and arr[i]==arr[i-1]): continue
            for j in range(i+1,n):
                if(j!=i+1 and arr[j]==arr[j-1]): continue
                k=j+1
                l=n-1
                while(k<l):
                    s=arr[i]
                    s+=arr[j]
                    s+=arr[k]
                    s+=arr[l]
                    if s==target:
                        li=[arr[i],arr[j],arr[k],arr[l]]
                        ans.append(li)
                        k+=1
                        l-=1
                        while(k<l and arr[k]==arr[k-1]):k+=1
                        while(k<l and arr[l]==arr[l+1]):l-=1
                    elif s<target:k+=1
                    else:l-=1
        return ans
