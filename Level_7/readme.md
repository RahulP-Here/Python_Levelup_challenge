[Scroll Down](#end)

# PYTHON : 10 DAYS LEVEL-UP CHALLANGE [DAY-7]

## 7. Library Management System !

Congratulations!.. We're completed 6 levels.

On day 7 we will create a dashboard for manage library : `Library Management System`. In this program we create a class called library which includes different methods which help to manage our library. Also we create a interactive user dashboard for easy management.

The Dashboard includes functionalities to create a library and add, delete or show the books of library.

#### Require Topics :
- [Classes and Objects in Python](https://www.w3schools.com/python/python_classes.asp)
- [Python termcolor module](https://pypi.org/project/termcolor/)  
- [Python \_\_init\_\_ Method](https://www.w3schools.com/python/gloss_python_class_init.asp)  
- [Getter & Setters](https://www.geeksforgeeks.org/getter-and-setter-in-python/)  
- [Dynamic Variable in Python](https://www.geeksforgeeks.org/python-program-to-create-dynamically-named-variables-from-user-input/)  
- [Logical Operators](https://www.w3schools.com/python/gloss_python_logical_operators.asp)  


so here we go...

<br>

---

**Steps :**

- ### 1. Library Class
    - [Create Library Class](#create-library-class)
    - [Set init method](#set-init-method)
    - [Set Other Methods](#set-other-methods)
        - [Method for Add Books](#method-for-add-books)
        - [Method for Delete Books](#method-for-delete-books)
        - [Method for Show Books](#method-for-show-books)
    - [Set a Getter](#set-a-getter)

- ### 2. User Dashboard
    - [Import Class](#import-class)
    - [Create Library](#create-library)
    - [Create Dashboard](#create-dashboard)

---

- ### 3. [Output](#output)

---

- ### Logic Template
    - [Library Class](#logic-template-library-class)
    - [User Dashboard](#logic-template-user-dashboard)
    - [Dashboard Work Flow](#work-flow-chart-of-dashboard)


---          
---

<br>

## 1. Library Class

A Library Class has all the methods regarding to manage the library via user dashboard.

- ### Create Library Class
    In python [Class](https://www.w3schools.com/python/python_classes.asp) is a code template for creating objects.
    we create a library class to create a library [Object](https://www.w3schools.com/python/python_classes.asp) 

```python
    class Library:
        pass

```
---

- ### Set Init Method
    -  The python [\_\_init\_\_ method](https://www.w3schools.com/python/gloss_python_class_init.asp) is declared within a class and is used to initialize the attributes of an object as soon as the object is formed.

    - Inshort this method autometically call everytime whenever new object created.

```python
    class Library:
        #Initialize new Library object
        def __init__(self):
            self.books  = []
            print(colored("------>  !!Library Created       Seccessfully!!", 'green'))

```

> We initialize a empty book list for storing book in future. 
---
- ### Set Other Methods
    In the next Step we Create other impoertant method of class that perform add, shiw and delete for books in the library.

    - #### Method for Add Books
        I.   This method help to add books in the library.  
        II.  Return number of added books.

    - #### Method for Delete Books
        I.    This method help to delete books from library.  
        II.   Show Warning if entered book not found.    
        III.  Return number of deleted books.  

    - #### Method for Show Books
        I.    This method help to print list of books avilable in the library  
        II.   Show warning if library is empty.
        

```python
    #Add Books to Libraby
    def addBooks(self, book_name):
        #code
        return "num of added book"

    #Delete Books from Libraby
    def delBooks(self, book_name):
        if(book in library):
            #code
            return "num of deleted book"
        else:
            #code
            return "Not found"
            
    #Show books of Library
    def showBooks(self):
        if(self.books is empty):
            print("Sorry Librabry is empty")
        else:
            #print list of book

    #ADD THEM INTO CLASS
```

> Note : Here in all class method there is a attribute called [Self](https://www.geeksforgeeks.org/self-in-python-class/). It is a default parameter, named 'self' is always passed in its argument. This self represents the object of the class itself. 

---

- ### Set a Getter
    -  In Python [Getters](https://www.geeksforgeeks.org/getter-and-setter-in-python) are the methods used in Object-Oriented Programming (OOPS) which helps to access the private attributes from a class.

    - It helps to directly use `total number of book` as a class variable without any method of function call.

```python
    #Getter:         
    @property
    def total(self):
        return len(self.books)

    #ADD THIS INTO CLASS
```

> Note : For initialize a [Getter](https://www.geeksforgeeks.org/getter-and-setter-in-python) method we use a [Method Decorator](https://peps.python.org/pep-0318/) `@property`.  

>Note : A [Decorator](https://peps.python.org/pep-0318/) is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure

---
###### Logic Template (Library Class)
```python
    class Library:
        #Initialize new Library object
        def __init__(self):
            self.books  = []
            print(colored("------>  !!Library Created Seccessfully!!", 'green'))
        
        #Add Books to Libraby
        def addBooks(self, book_name):
            #code
            return "num of added book"

        #Delete Books from Libraby
        def delBooks(self, book_name):
            if(book in library):
                #code
                return "num of deleted book"
            else:
                #code
                return "Not found"
                
        #Show books of Library
        def showBooks(self):
            if(self.books is empty):
                print("Sorry Librabry is empty")
            else:
                #print list of book
        
        #Getter:         
        @property
        def total(self):
            return len(self.books)
```
---
---

<br>
     
## 2. User Dashboard

- ### Import Class
    We need to import our library class for link dashboard functionalities with class methods.

    ```python
        from termcolor import colored #coloring font in Terminal 
        from Library import Library #Librabry Class
    ```

> Note : To change the text color, we use a Python library called [Termcolor](https://pypi.org/project/termcolor/) 

> Note: To install termcolor use -- `pip install termcolor`

- ### Create Library
    Here we are using the [globals](https://www.geeksforgeeks.org/python-program-to-create-dynamically-named-variables-from-user-input/) method for creating a dynamically named Library (`variable`) and later assigning it a library object

  ```python
        def create_Library(lib_Name):
            globals()[lib_Name] = Library()

        #Create Library Object
        library = input("Enter Your Library name : ")
        create_Library(library)
  ```

- ### Create Dashboard

    Now we Create Out User Dashboard which perform specific functionalities like :
    - i.   Creating A Library
    - ii.  Entering To User Dashboard
    - iii. Quit From Dashboard
    - iv.  Show Books
    - v.   Add Books
    - vi.  Delete Books

    The whole dashboard creation is possible with loops.

###### Logic Template (User Dashboard)
```python
    from termcolor import colored #coloring font in Terminal 
    from Library import Library #Librabry Class

    def create_Library(lib_Name):
            globals()[lib_Name] = Library()

    # -----------------
    #START
    print("WELCOME TO LIBRABRY MANAGEMENT SYSTEM".center(100, "-"))

    #Create Library Object
    library = input("Enter Your Library name : ")
    create_Library(library)

    #w-loop-1
    while(True):
        #Entering Into Library
        print(colored("\n     1. Library DashBoard\n     2. Quit Program\n", 'blue'))
        
        #Entering Into Dashboard
        if((user := input("Enter : ")) == "1"):
            
            #w-loop-2
            while(True):
                #Dashboard Menu
                print(colored("\n     >> DASHBOARD", 'yellow'))
                print(colored("     1. Show Books\n     2. Add Books\n     3. Delete Books\n     4. Quit\n", 'blue'))
                user  = input()
                if(user == "1"):
                    #1. Show Books of Library
                    globals()[library].showBooks()

                elif(user == "2" or user == "3"):    
                    book = input("bookname")
                    if(user == "2")
                        #2. Add Books in Library
                        globals()[library].addBooks()
                    else:
                        #3. Delete Books from Library
                        globals()[library].delBooks()

                elif(user == "4"):    
                    #4. Quit
                    break #[end of w-loop-2]
            break #[direct end of w-loop-1]
                else:
                    #invalid Input

    #END
    print("     THANKS TO VISIT     ".center(100, "-")) 
```
> Additional Functionalities :
>   - If Library is Empty, `diable Show / Delete`
>   - If Num of deleting book > total book, `diable Delete`
>   - If Enterted book not found, `Show Not Found Warning`

### ` Work Flow-Chart OF Dashboard `
[Work Flow Diagram](/img/Level7_output/Untitled%20Diagram.drawio.pdf)
![Work Flow Diagram](/img/Level7_output/ex7.drawio.png)

> NOTE :  
>   - [colored()](https://pypi.org/project/termcolor/0.2/) is method  of [Termcolor](https://pypi.org/project/termcolor/) to coloring output text. `print(colored("This s Red", 'red'))`
>
>   - `globals()[library]` is a variable instance to call a [dynamic variable](https://www.geeksforgeeks.org/python-program-to-create-dynamically-named-variables-from-user-input/)
>
>   - ` := ` is [Walrus Operator](https://www.geeksforgeeks.org/walrus-operator-in-python-3-8/), that offers a way to assign to variables within an expression, including variables that do not exist yet

---
---

<br>
     
##  output  
#### Create a Library :  
![image](/img/Level7_output/create.png) 

#### User Dashboard :  
![image](/img/Level7_output/dashboard.png) 

#### Empty Library :  
![image](/img/Level7_output/empty.png) 

#### Add - Del - Show :  
![image](/img/Level7_output/main.png) 

#### Quit Dashboard :  
![image](/img/Level7_output/quit.png) 
---

Code : 

[Exercise 7](exe7_Dashboard.py)

[Library Class](Library.py)

<br>

###### END


> See You In Level 8 👀....
