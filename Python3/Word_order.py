n = int(input())
d = {}
for i in range(n):
    a = input()
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
print(len(d))
print(*d.values())



'''
Sample Input

4
bcdef
abcdefg
bcde
bcdef

Sample Output

3
2 1 1

'''
