m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
print(len(a.symmetric_difference(b)))


'''
Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output

8

'''
