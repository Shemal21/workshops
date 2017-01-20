# create your simple Book class in this file

class Book(object):
    def __init__(self, title = '', author = '', pages = 0, status = 'r'):
        self.title = title
        self.author = author
        self.pages = pages
        self.status = status
    def __str__(self):
        return self.title + ' ' + self.author + ' ' + str(self.pages) + ' ' + self.status
        #return '{}, {}, {:d}, {}'.format(self.title, self.author, self.pages, self.status)

    def mark_book_completed(self):
        self.status = 'c'

    def is_long_book(self):
        return self.pages >= 500











