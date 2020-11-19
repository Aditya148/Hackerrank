from collections import defaultdict
n, m = [int(i) for i in input().split()]
l1 = []
d = defaultdict(list)

for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    l1.append(input())
  
for i in l1:
    if i in d:
        print(' '.join([str(j) for j in d[i]]))
    else:
        print(-1)
        
        

'''
Sample Input

5 2
a
a
b
a
b
a
b

Sample Output

1 2 4
3 5

'''
