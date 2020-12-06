import numpy as np

r, c = [int(i) for i in input().split()]
a = []
for i in range(r):
    a.append([int(j) for j in input().split()])
print(np.transpose(a))
print(np.array(a).flatten())




'''
Sample Input

2 2
1 2
3 4

Sample Output

[[1 3]
 [2 4]]
[1 2 3 4]

'''
