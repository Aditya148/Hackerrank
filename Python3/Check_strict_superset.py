a = set(map(int, input().split()))
n = int(input())
count = 0
for i in range(n):
    s = set(map(int, input().split()))
    if s.issubset(a):
        count += 1
if count == n:
    print('True')
else:
    print('False')
    
    
    
    
'''
Sample Input 0

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output 0

False


'''
