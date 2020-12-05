import numpy as np
n, m = tuple(map(int, input().split()))
np.set_printoptions(sign=' ')
print(np.eye(n, m, k = 0))




'''
Sample Input

3 3

Sample Output

[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]

'''
