'''
You are given three integers x,n,m. Your task is to find pow(x,n) mod m in O(1)

Sample Input 1 :
2 
3 1 2
4 3 10
Sample Output 1 :
1
4
Explanation For Sample Output 1:
In test case 1, 
X = 3, N = 1, and M = 2 
X ^ N = 3 ^ 1 = 3 
X ^ N % M = 3 % 2 = 1. 
So the answer will be 1.

In test case 2,
X = 4, N = 3, and M = 10 
X ^ N = 4 ^ 3 = 64 
X ^ N % M = 64 % 10 = 4. 
So the answer will be 4.
'''

def modularExponentiation(x, n, m):
	# Write your code here.  
	res = 1 
	x = x % m
	while (n > 0):
		if ((n & 1) == 1):
			res = (res * x) % m
		n = n >> 1
		x = (x * x) % m
	return res
