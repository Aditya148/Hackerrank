x, k = [int(i) for i in input().split()]
exp = input()
a = eval(exp.replace('x', str(x)))
if a==k:
    print('True')
else:
    print('False')
    
    
    
    
'''
Sample Input

1 4
x**3 + x**2 + x + 1

Sample Output

True

'''
