#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    lst = []
    for i in range(4):
        for j in range(4):
            r1 = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            r2 = arr[i+1][j+1]
            r3 = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            lst.append(r1+r2+r3)
    return max(lst)
            
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()



'''
Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output

19

'''
