#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N%2 != 0:
        print('Weird')
    elif N%2 == 0:
        if N in range(2,6):
            print('Not Weird')
        if N in range(6,21):
            print('Weird')
        if N>20:
            print('Not Weird')
            
            
'''
Sample Input 0

3

Sample Output 0

Weird

Sample Input 1

24

Sample Output 1

Not Weird

'''
