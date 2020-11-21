def sumUnderModulo(a,b):
    return (a+b)%((10**9)+7)
    
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a,b = map(int,input().strip().split())
        print(sumUnderModulo(a,b))
