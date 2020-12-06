n, x = [int(i) for i in input().split()]
sub = []
for _ in range(x):
    sub.append([float(i) for i in input().split()])
for i in zip(*sub):
    print(float(sum(i)/x))





'''
Sample Input

5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

Sample Output

90.0 
91.0 
82.0 
90.0 
85.5        

'''
