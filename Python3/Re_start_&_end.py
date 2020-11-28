string = str(input())
sub = str(input())
l = len(sub)
if sub not in string:
    print((-1, -1))
else:
    for i in range(0,len(string)-l+1):
        if string[i:i+len(sub)] == sub:
            if l == 1:
                t = (i, i)
            else:
                t = (i, i+len(sub)-1)
            print(t)
        
        
'''
Sample Input

aaadaa
aa

Sample Output

(0, 1)  
(1, 2)
(4, 5)

'''
