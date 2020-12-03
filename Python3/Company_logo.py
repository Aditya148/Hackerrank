#!/bin/python3

import math
import os
import random
import re
import sys



from collections import Counter

class OrderedCounter(Counter):
    pass

[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]





'''
Sample Input 0

aabbbccde

Sample Output 0

b 3
a 2
c 2


'''
