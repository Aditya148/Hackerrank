import numpy as np
n, m = [int(i) for i in input().split()]
arr = []
for _ in range(n):
    arr.append([int(i) for i in input().split()])
print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(round(np.std(arr), 11))




'''
Sample Input

2 2
1 2
3 4

Sample Output

[ 1.5  3.5]
[ 1.  1.]
1.11803398875

'''
