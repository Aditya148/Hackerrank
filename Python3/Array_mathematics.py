import numpy as np
n, m = [int(i) for i in input().split()]
a = []
b = []
for _ in range(n):
    a.append([int(i) for i in input().split()])
for _ in range(n):
    b.append([int(i) for i in input().split()])
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.array(a)//np.array(b))
print(np.mod(a,b))
print(np.power(a,b))




'''
Sample Input

1 4
1 2 3 4
5 6 7 8

Sample Output

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 

'''
