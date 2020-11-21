t = int(input())
for i in range(t):
    n, d = input().split()
    try:
        print(int(int(n)/int(d)))
    except ValueError as e:
        print('Error Code:', e)
    except ZeroDivisionError as e:
        print('Error Code: integer division or modulo by zero')
        
        
'''
Sample Input

3
1 0
2 $
3 1

Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3

'''
