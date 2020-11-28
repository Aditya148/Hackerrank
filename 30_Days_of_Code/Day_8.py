n = int(input())
records = [input().split() for _ in range(n)]
d = {k: v for k,v in records}
while True:
    try:
        name = input()
        if name in d:
            print(name + '=' + d[name])
        else:
            print('Not found')
    except:
        break
        
        
'''
Sample Input

3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Sample Output

sam=99912222
Not found
harry=12299933

'''
