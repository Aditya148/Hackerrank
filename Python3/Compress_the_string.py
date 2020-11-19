from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])


'''
Sample Input

1222311

Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)

'''
