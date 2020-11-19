from itertools import combinations
S, K = input().split()
new = ''.join(sorted([i for i in S]))
for j in range(1,int(K)+1):
    for i in combinations(new, int(j)):
        print(''.join(i))
        
        
'''
Sample Input

HACK 2

Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK

'''
