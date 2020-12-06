import re
t = int(input())
for _ in range(t):
    if re.match(r'[789]\d{9}$', input()):   
        print('YES')
    else:  
        print('NO') 
        
        
        
'''
Sample Input

2
9587456281
1252478965

Sample Output

YES
NO

'''
