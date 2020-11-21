import re, sys
s = sys.stdin
ans = []
for i in s:
    for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', i, re.I):
        ans.append(j)
for i in ans:
    print(i)



'''
Sample Input

11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   

Sample Output

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

'''
