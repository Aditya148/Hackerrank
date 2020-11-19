from itertools import permutations
S, K = input().split()
lst = permutations([i for i in S], int(K))
new = []
for i in lst:
    new.append(''.join(i))
for i in sorted(new):
    print(i)
    
    
'''
Sample Input

HACK 2

Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

'''
