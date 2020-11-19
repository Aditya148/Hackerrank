from collections import Counter
X = int(input())
L = [int(i) for i in input().split()]
N = int(input())
D = Counter(L)
sum = 0
for i in range(N):
    s, p = [int(i) for i in input().split()]
    if s in D and D[s]>0:
        sum += p
        D[s] -= 1
print(sum)



'''
Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output

200

'''
