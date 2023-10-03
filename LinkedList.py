class Book():
    def __init__(self, bid, title, author, status):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = status

    def __str__(self):
        print(f'Book id: {self.bid}')
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Status: {self.status}')

class Node:
    def __init__(self, value: Book):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head:
            return False
        else:
            return True

    def addBook(self, book):
        node = Node(book)
        if self.searchBook(book.bid) < 0:
            if self.isEmpty():
                self.head = node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = node

    def searchBook(self, bid):
        '''
        :param bid: book id
        :return: If book found, return the book's index in the linked list. Return -1 otherwise.
        '''
        if self.isEmpty():
            return -1
        else:
            temp = self.head
            i =0
            while temp:
                i+=1
                if temp.value.bid == bid:
                    return i
                temp = temp.next
            return -1

    def deleteBook(self, bid):
        '''
        :param bid: book id
        :return: data of the book deleted
        '''
        if self.isEmpty():
            return None
        else:
            if self.head.value.bid == bid:
                value = self.head.v
                self.head = self.head.next
                if self.isEmpty():
                    return value
                return value
            else:
                temp = self.head
                while temp.next:
                    if temp.next.value.bid == bid:
                        value = temp.next.value
                        temp.next = temp.next.next
                        return value
                    temp = temp.next
                return None


    def traverse(self):
        temp = self.head
        while temp:
            temp.value.__str__()
            temp=temp.next

book1 = Book(3,'haha', 'ngoc chau', 'avail')
book2 = Book(4,'ha', 'chau', 'avail')
book3 = Book(5,'haa', 'ngoc', 'avail')
booklist = LinkedList()
booklist.addBook(book1)
booklist.addBook(book2)
booklist.addBook(book3)
print(booklist.searchBook(7))
booklist.deleteBook(bid=5)

booklist.traverse()