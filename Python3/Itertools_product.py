from itertools import product

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
ans = list(product(A,B))
for i in ans:
    print(i, end=' ')


'''
Sample Input

 1 2
 3 4

Sample Output

 (1, 3) (1, 4) (2, 3) (2, 4)

'''
