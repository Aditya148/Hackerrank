from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        l = len(data.split('\n'))
        if l>1:
            print(">>> Multi-line Comment")
        elif l==1:
            print(">>> Single-line Comment")
        if data.strip():
            print(data)
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()




'''
Sample Input

4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->

Sample Output

>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]

'''
