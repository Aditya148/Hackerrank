import math
ab = float(input())
bc = float(input())
ac=math.hypot(ab, bc)                      
ang=round(math.degrees(math.acos(bc/ac))) 
degree=chr(176)                           
print(ang, degree, sep='')


'''
Sample Input

10
10

Sample Output

45°

'''
