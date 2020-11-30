#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    print(len(max(bin(n).split('b')[1].split('0'))))
    
    
    
'''
Sample Input 1

5

Sample Output 1

1

Sample Input 2

13

Sample Output 2

2

'''
