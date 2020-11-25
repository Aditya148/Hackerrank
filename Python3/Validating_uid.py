import re

#    (?!.*(.).*\1) checks no repeating characters;
#    (?=(?:.*[A-Z]){2,}) checks at least 2 uppercase letters;
#    (?=(?:.*\d){3,}) checks at least 3 digits;
#    [a-zA-Z0-9]{10} checks exactly 10 alphanumeric characters.

[print('Valid') if re.match(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$', input()) else print('Invalid') for _ in range(int(input()))]



'''
Sample Input

2
B1CD102354
B1CDEF2354

Sample Output

Invalid
Valid

'''
