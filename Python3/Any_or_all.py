n = int(input())
arr = input().split()
print(any([i[:]==i[-1::-1] for i in arr]) and all([int(i)>0 for i in arr]))



'''
Sample Input

5
12 9 61 5 14 

Sample Output

True
'''
