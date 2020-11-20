import calendar
m, d, y = map(int, input().split())
a = calendar.weekday(y, m, d) 
print(calendar.day_name[a].upper())



'''
Sample Input

08 05 2015

Sample Output

WEDNESDAY

'''
