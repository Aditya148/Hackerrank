import statistics
n = int(input())
arr = [int(i) for i in input().split()]
mean = sum(arr)/n
var = sum([(i-mean)**2 for i in arr])/n
print(round(var**0.5, 1))



'''
Sample Input

5
10 40 30 50 20

Sample Output

14.1

'''
