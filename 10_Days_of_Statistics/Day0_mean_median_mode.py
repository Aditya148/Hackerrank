import numpy as np
from scipy import stats
n = int(input())
a = [int(i) for i in input().split()]
print(np.mean(a))
print(np.median(a))
print(stats.mode(a)[0][0])



'''
Sample Input

10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

Sample Output

43900.6
44627.5
4978

'''
