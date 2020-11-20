n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    a = input().split()
    if 'pop' in a:
        s.pop()
    else:
        eval('s.{}({})'.format(a[0], a[1]))
print(sum(s))



'''
Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Sample Output

4

'''
