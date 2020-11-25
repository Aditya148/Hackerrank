from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attr):
        print(tag)
        for att in attr:
            print('-> {} > {}'.format(att[0], att[1]))
                
parser = MyHTMLParser()
for i in range(int(input())):
    parser.feed(input())
    
    
'''
Sample Input

9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>

Sample Output

head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high

'''
