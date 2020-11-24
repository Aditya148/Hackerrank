from itertools import product
k, m = map(int, input().split())
a = []
a = (list(map(int, input().split()))[1:] for _ in range(k))
results = map(lambda x: sum(i**2 for i in x)%m, product(*a))
print(max(results))



'''
Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

Sample Output

206

'''
