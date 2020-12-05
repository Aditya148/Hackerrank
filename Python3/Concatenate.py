import numpy as np

N, M, P = [int(i) for i in input().split()]
arrA = np.array([input().split() for _ in range(N)],int)
arrB = np.array([input().split() for _ in range(M)],int)
print(np.concatenate((arrA, arrB), axis = 0))





'''
Sample Input

4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 

Sample Output

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 

'''
