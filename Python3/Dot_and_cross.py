import numpy as np

n = int(input())
a = []
b = []
for i in range(n):
    a.append([int(i) for  i in input().split()])
for i in range(n):
    b.append([int(i) for  i in input().split()])
print(np.dot(a,b))





'''
Sample Input

2
1 2
3 4
1 2
3 4

Sample Output

[[ 7 10]
 [15 22]]

'''
