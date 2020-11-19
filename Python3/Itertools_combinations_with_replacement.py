from itertools import combinations_with_replacement
S, K = input().split()
new = ''.join(sorted([i for i in S]))
for i in combinations_with_replacement(new, int(K)):
    print(''.join(i))
    
    
'''
Sample Input

HACK 2

Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK

'''
