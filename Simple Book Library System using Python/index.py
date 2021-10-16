class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have borrow a {bookName} book. Return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book has already been borrow by someone else. Please borrow another book available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book!")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         

if __name__ == "__main__":
    centraLibrary = Library(["PHP", "JavaScript", "VB.net", "Python"])
    student = Student()
   
    while(True):
        welcomeMsg = '''\n ====== Book Library System+ ======
        Please choose an option:
        1. Display all the books
        2. Borrow book
        3. Return book
        4. Exit 
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")

        
