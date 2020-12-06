import numpy as np

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
print(np.inner(a,b))
print(np.outer(a,b))




'''
Sample Input

0 1
2 3

Sample Output

3
[[0 0]
 [2 3]]

'''
