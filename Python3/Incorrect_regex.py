import re
t = int(input())
for i in range(t):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)
        
        
'''
Sample Input

2
.*\+
.*+

Sample Output

True
False

'''
