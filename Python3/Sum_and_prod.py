import numpy as np
n, m = [int(i) for i in input().split()]
arr = []
for _ in range(n):
    arr.append([int(i) for i in input().split()])
print(np.prod(np.sum(arr, axis = 0)))



'''
Sample Input

2 2
1 2
3 4

Sample Output

24

'''
