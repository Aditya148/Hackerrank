import re

n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())

for z in zip(*a):
    b += "".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))


'''
Sample Input 0

7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!

Sample Output 0

This is Matrix#  %!

Explanation 0

The decoded script is:

This$#is% Matrix#  %!

'''
