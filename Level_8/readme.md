[Scroll Down](#end)

# PYTHON : 10 DAYS LEVEL-UP CHALLANGE [DAY-8]

## 8. Clear The Clutter !

Congratulations!.. We're completed 7 levels of challange.

Welcome to Day 8 of the Python 10 Days Level-Up Challenge! In today's exercise, we've created a program that helps you `Clear The Clutter` in a specified folder. 

The program is interactive with the help of dashboard, that allows you to perform operations like clearing clutter, displaying all files, and showing specific format files.

>###  `What is Clutter?`
>
>Clutter is essentially the disorganization of your data, files and digital devices. This mess can appear in many forms — like a crowded inbox.

### Before:
![image](/img/Level8_output/cluttered%20folder.png)

### After:
![image](/img/Level8_output/After%20Clutter%20folder.png)

#### Require Module :
- [os](https://docs.python.org/3/library/os.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [time](https://docs.python.org/3/library/time.html)
- [termcolor](https://pypi.org/project/termcolor/) 

Let's explore the details...

<br>

---

**Steps :**

- ### 1. Folder Class
    - [OS Module](#import-os-module)
    - [Initialize Folder Class](#1-folder-class-1)
    - [Set init method](#initialization-__init__)
    - [Set Other Methods](#set-other-methods)
        - [Clear Clutter in Folder](#clearclutter-method)
        - [Show Specific Format Files](#showfiles-method)
        - [Show All Files](#showallfiles-method)

- ### 2. User Dashboard
    - [Import Class](#import-class)
    - [Create Folder Object](#create-folder-object)
    - [Create Dashboard](#create-dashboard)

---

- ### Logic Template
    - [Folder Class](#logic-template-folder-class)
    - [User Dashboard](#logic-template-user-dashboard)

---

- [Output](#output)

---          
---

<br>

## 1. Folder Class

A Folder Class has all the methods for list files and clear the clutter.

- ### Import Os Module
    Python has a built-in os module with methods for interacting with the operating system, like creating files and directories, management of files and directories, input, output, environment variables, process management
 
```python
    import os
```

```python
    #Methods of OS Module

    os.listdir(path) #list names of all the files present in the specified path

    os.rename(old, new) #rename a file or directory
```
---

- ### Initialize Folder Class
    Create a class named `Folder` that represents a folder and contains methods for clearing clutter, showing files with a specific extension, and showing all files.
 
```python
    class Folder:
        # Implementation of the Folder class...
        pass

```
---

- ### Initialization (`__init__`)
    - Takes a folder path as input.
    - Attempts to get the list of files in the folder and extract the folder name from the path.
    - Prints a success message or an error message if the path is invalid.

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

    - #### `clearClutter` Method
        I.   Takes `Extension` and `name` as parameters.
        II.  Creates a list of files in the folder with the specified extension.
        III. Renames each file with the provided name and an index.
        IV.  Prints the list of cleared files and a success message.
        V.   If no files are found, prints a message indicating the absence of files with the specified extension.
        VI.  Updates the list of files in the folder.

    - #### `showFiles` Method
        I.   Takes `Extension` as a parameter.
        II.  Displays files with the specified extension, along with an index.
        III. Prints a message if no files are found with the specified extension.  

    - #### `showAllFiles` Method:
        I.   Displays all files in the folder along with an index.
        II.  Prints a message if the folder is empty.
        

```python
    def clearClutter(self, Extension, name):
        # Method to clear clutter by renaming files...

    def showFiles(self, Extension):
        # Method to display files with a specific extension...

    def showAllFiles(self):
        # Method to display all files in the folder...

    #ADD THEM INTO CLASS
```

> Note : Here in all class method there is a attribute called [Self](https://www.geeksforgeeks.org/self-in-python-class/). It is a default parameter, named 'self' is always passed in its argument but other attributes like `Extension` have to pass manually.

---
###### Logic Template (Folder Class)
```python
    import os
    from termcolor import colored

    class Folder:
    def __init__(self, path):
        self.path = path
        '''
        list all files using os.listdir()
        '''

    def clearClutter(self, Extension, name):
        # Method to clear clutter by renaming files...
        '''
        1. list all files that ends with extension using os.listdir()

        2.rename them all via os.rename()
        '''
        

    def showFiles(self, Extension):
        # Method to display files with a specific extension...
        '''
        print list of Extension files in directory.
        '''

    def showAllFiles(self):
        # Method to display all files in the folder...
        '''
        print list of All files in directory.
        '''
```

> [Methods Of Os Module](#import-os-module)
---
---

<br>
     
## 2. User Dashboard

- ### Import Class
    We need to import our `Folder Class` for link dashboard functionalities with class methods.

    ```python
        from termcolor import colored #coloring font in Terminal 
        from FolderClass import * #Folder Class
    ```

> Note : To change the text color, we use a Python library called [Termcolor](https://pypi.org/project/termcolor/) 

> Note: To install termcolor use -- `pip install termcolor`

- ### Create Folder Object

  ```python
    #Create Object of Folder class
    path = input('Enter Path of Folder: ')
    f = Folder(path)
  ```

- ### Create Dashboard

    Now we Create Out User Dashboard which perform specific functionalities like :
    - i.   List files of directory
    - ii.  Clear Clutter
    - iii. Exit

    The whole dashboard created in while loop to repeart iteration.

###### Logic Template (User Dashboard)
```python
    from termcolor import colored #coloring font in Terminal 
    from FolderClass import * #Folder Class

    #------------ USER DASHBOARD -------------      

    #Create Object of Folder class
    path = input('Enter Path of Folder: ')
    f = Folder(path)

    while(True):
        print(colored("\nPress >>>", 'light_yellow'))
        print(colored("    1. Clear Clutter\n    2. Show All Files\n    3. Show Specific Format Files\n    4.Exit\n", 'light_yellow'))
        user = input('\r    Enter: ').strip()

        if(user == '1'):
            format = input("Format of files : ").lower()
            new_name = input("Identified Name : ") 

            f.clearClutter(format, new_name)

        elif(user == '2'): 
            f.showAllFiles()

        elif(user == '3'): 
            format = input("Format of files You wanna list : ").lower()
            f.showFiles(format)

        elif(user == '4'): 
            break

        else: 
            print(colored("Invalid Input !", 'red'))

    #END
    print("     THANK YOU     ".center(100, "-")) 
```

> Additional Functionalities :
>   - The program dynamically handles invalid inputs and provides feedback to the user.
>
>- The loading animation is a visual indicator of ongoing processes within the program.
>
>- The Folder class methods ensure that the user receives relevant information about the operations performed.

---
---

<br>
     
##  output  
#### Create Folder Object :  
![image](/img/Level8_output/folder%20in%20operation%20mode.png) 

#### User Dashboard :  
![image](/img/Level8_output/dashboard.png) 

#### Show All Files :  
![image](/img/Level8_output/2.png) 

#### Before Clear Clutter :  
![image](/img/Level8_output/unclear%20clutter.png) 

#### Clear The Clutter :  
![image](/img/Level8_output/1.png) 

#### After Clear Clutter :  
![image](/img/Level8_output/clear%20clutter.png) 

#### Exit :  
![image](/img/Level8_output/exit.png) 

<br>

---


Code :
[Exercise 8](exe8.py)

[Folder Class](FolderClass.py)

###### END


> See You In Level 9 👀....
