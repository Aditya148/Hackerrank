a = int(input())
m = sorted(set(map(int, input().split())))
b = int(input())
n = sorted(set(map(int, input().split())))
ans = []
for i in m:
    if i not in n:
        ans.append(i)
for i in n:
    if i not in m:
        ans.append(i)
for i in sorted(ans):
    print(i)



'''
Sample Input

4
2 4 5 9
4
2 4 11 12

Sample Output

5
9
11
12

'''
