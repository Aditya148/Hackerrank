import numpy as np
n, m = [int(i) for i in input().split()]
arr = []
for _ in range(n):
    arr.append([int(i) for i in input().split()])
b = np.min(arr, axis=1)
print(max(b))



'''
Sample Input

4 2
2 5
3 7
1 3
4 0

Sample Output

3

'''
