'''LIBRARY CLASS'''

from termcolor import colored #Termcolor : coloring font in Terminal 

class Library:
    #Initialize new Library object
    def __init__(self):
        self.books  = []
        print(colored("------>  !!Library Created Seccessfully!!", 'green'))

    #Add Books to Libraby
    def addBooks(self, book_name):
        self.books = self.books + list(book_name)
        return f"Successfully Added {len(book_name)} Books!"

    #Delete Books from Libraby
    def delBooks(self, book_name):
        n = 0
        for book in book_name:
            try:
                self.books.remove(book)            
                n = n+1
            except:
                 print(colored(f"!!({book}) not found!!", 'red'))
        return f"Successfully Deleted {n} Books!"
        
    #Show books of Library
    def showBooks(self):
        if(len(self.books)==0):
             print("Sorry Librabry is empty")
        else:
            for index,book in enumerate(self.books, start=1):
                print(f"{index}. {book}")

    #Getter: to dynamically Access size of library after every change         
    @property
    def total(self):
         return len(self.books)