from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super(Book, self).__init__()
        self.price = price
    def display(self):
        print('Title:', title)
        print('Author:', author)
        print('Price:', price)

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()




'''
Sample Input

The following input from stdin is handled by the locked stub code in your editor:

The Alchemist
Paulo Coelho
248

Sample Output

The following output is printed by your display() method:

Title: The Alchemist
Author: Paulo Coelho
Price: 248

'''
