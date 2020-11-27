from statistics import median
n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
l = int(len(arr)/2)
if len(arr)%2 == 0:
    q1 = arr[:l]
    q3 = arr[l:]
else:
    q1 = arr[:l]
    q3 = arr[l+1:]
print(int(median(q1)))
print(int(median(arr)))
print(int(median(q3)))



'''
Sample Input

9
3 7 8 5 12 14 21 13 18

Sample Output

6
12
16

'''
