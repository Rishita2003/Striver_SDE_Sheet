'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
'''
from os import *
from sys import *
from collections import *
from math import *

def zeroMatrix(matrix, n, m):
    # Write your code here.
    m=len(matrix)
    n=len(matrix[0])
    x=1
    y=1
    for j in range(n):
        if matrix[0][j]==0:
            x=0
    for i in range(m):
        if matrix[i][0]==0:
            y=0
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j]==0:
                matrix[i][0]=0
                matrix[0][j]=0
    for j in range(1,n):
        if matrix[0][j]==0:
            for i in range(0,m):
                matrix[i][j]=0
    for i in range(1,m):
        if matrix[i][0]==0:
            for j in range(0,n):
                matrix[i][j]=0
    if y==0:
        for i in range(m):
            matrix[i][0]=0
    if x==0:
        for j in range(n):
            matrix[0][j]=0
    

    return matrix
    pass
