from itertools import combinations

N = int(input())
L = input().split()
K = int(input())

C = list(combinations(L, K))
F = filter(lambda c: 'a' in c, C)
print("{0:.3}".format(len(list(F))/len(C)))




'''
Sample Input

4 
a a c d
2

Sample Output

0.8333

'''
