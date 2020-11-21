import math
class Solution:
    def getSmallestDivNum(self, n): 
        l = [int(i) for i in range(1,n+1)]
        lcm = l[0]
        for i in range(1,len(l)):
            lcm = lcm*l[i]//math.gcd(lcm, l[i])
        return lcm

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        ob = Solution()
        print(ob.getSmallestDivNum(n))
