n, m = map(int, input().split())
arr = input().split()
a = set(input().split())
b = set(input().split())
print(sum((i in a)-(i in b) for i in arr))



'''
Sample Input

3 2
1 5 3
3 1
5 7

Sample Output

1

'''
