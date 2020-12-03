t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(i) for  i in input().split()]
    i = 0
    while i < n-1 and arr[i] >= arr[i+1]:
        i+=1
    while i < n-1 and arr[i] <= arr[i+1]:
        i+=1
    if i == n-1:
        print('Yes')
    else:
        print('No')
        
        
        
        
'''
Sample Input

2
6
4 3 2 1 3 4
3
1 3 2

Sample Output

Yes
No

'''
