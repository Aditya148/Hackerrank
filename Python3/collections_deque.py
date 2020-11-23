from collections import deque
n = int(input())
d = deque()
for i in range(n):
    a = input()
    if 'pop' in a:
        eval('d.{}()'.format(a))
    else:
        c, num = a.split()
        eval('d.{}({})'.format(c,num))
print(*d)



'''
Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output

1 2

'''
