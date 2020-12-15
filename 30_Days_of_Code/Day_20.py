#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
totalSwaps = 0
for i in range(n-1, 0, -1):
    numberOfSwaps = 0
    for j in range(i):           
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps += 1
            totalSwaps += 1
    if numberOfSwaps == 0:
        break
print('Array is sorted in {} swaps.'.format(totalSwaps))
print('First Element:', a[0])
print('Last Element:', a[-1])



'''
Sample Input 1

3
3 2 1

Sample Output 1

Array is sorted in 3 swaps.
First Element: 1
Last Element: 3


'''
