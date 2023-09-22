from abc import ABCMeta, abstractmethod

# Define the abstract base class Book
class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    @abstractmethod
    def display():
        pass

# Define the MyBook class which is a subclass of Book
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price
    
    def display(self):
        # Print the book details
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Price: {self.price}')

# Prompt the user to enter book details
title = input('Enter the title: ')
author = input('Enter the author: ')
price = int(input('Enter the price: '))

# Create a new instance of MyBook with the provided inputs
new_novel = MyBook(title, author, price)

# Display the book details
new_novel.display()