from collections import OrderedDict
n = int(input())
d = OrderedDict()
for i in range(n):
    item, space, price = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(price)
for item, price in d.items():
    print(item, price)




'''
Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

'''
