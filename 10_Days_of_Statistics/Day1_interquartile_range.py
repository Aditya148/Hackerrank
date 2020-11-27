from statistics import median
n = int(input())
arr = [int(i) for i in input().split()]
freq = [int(i) for i in input().split()]
lst = []
for i in range(n):
    for j in range(freq[i]):
        lst.append(arr[i])
lst.sort()
l = len(lst)//2
if len(lst)%2==0:
    q1 = lst[:l]
    q3 = lst[l:]
else:
    q1 = lst[:l]
    q3 = lst[l+1:]
print(round(float(median(q3) - median(q1)), 1))



'''
Sample Input

6
6 12 8 10 20 16
5 4 3 2 1 5

Sample Output

9.0

'''
