import re
for _ in range(int(input())):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))
    
    
    
'''
Sample Input 0

4
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output 0

False
True
True
False


'''
