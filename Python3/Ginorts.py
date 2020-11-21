s = input()
l = ''
u = ''
o = ''
e = ''
for i in s:
    if i.isalpha():
        if i.isupper():
            u += i
        else:
            l += i
    if i.isnumeric():
        if int(i)%2 == 0:
            e += i
        else:
            o += i
print(''.join(sorted(l)+sorted(u)+sorted(o)+sorted(e)))



'''
Sample Input

Sorting1234

Sample Output

ginortS1324

'''
