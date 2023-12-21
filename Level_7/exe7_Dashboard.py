''' EXERCISE - 7 : ! LIBRARY MANAGEMENT SYSTEM !'''

from termcolor import colored #Termcolor : coloring font in Terminal 
from Library import Library #Librabry Class : Created

#Dynamically Create Library
def create_Library(lib_Name):
    globals()[lib_Name] = Library()

#STARTING
print("WELCOME TO LIBRABRY MANAGEMENT SYSTEM".center(100, "-"))
print("")

#Create Library Object
library = input("Enter Your Library name : ")
create_Library(library)
print("\n..............")

#w-loop-1
while(True):
    #Entering Into Library
    print(colored("\n     1. Library DashBoard\n     2. Quit Program\n", 'blue'))
    
    #Entering Into Dashboard
    if((user := input("Enter : ")) == "1"):
        print(colored("------>  WELCOME TO DASHBOARD\n", 'yellow'))

        #w-loop-2
        while(True):
            #Dashboard Menu
            print(colored("\n     >> DASHBOARD", 'yellow'))
            print(colored("     1. Show Books\n     2. Add Books\n     3. Delete Books\n     4. Quit\n", 'blue'))

            #1. Show Books of Library
            if((dashboard_user := input("Enter : ")) == "1"):
                globals()[library].showBooks()

            #2/3. Delete or Add Books in Library
            elif(dashboard_user == "2" or dashboard_user == "3"):

                #if user delete book in empty librabry
                if(dashboard_user == "3" and globals()[library].total == 0):
                    print("Sorry Librabry is empty")

                else:
                    #w-loop-3
                    while(True):
                        #Enter number of books to del or add
                        print("Enter Number of Books want to ", end="") 
                        print("add : ", end="") if(dashboard_user == "2") else print("delete : ", end="") 

                        try:
                            books = int(input())

                            #Not as many books as the number entered
                            if(dashboard_user == "3" and globals()[library].total < books):
                                print(colored(f"Sorry! Total Number of Avialable books is only {globals()[library].total}\n", 'red'))
                                continue #skip the iteration and reask new number for book to delete

                            break #[end of w-loop-3]

                        except:
                            print(colored("Invalid : Please enter a valid Quantity!\n", 'red'))

                    #Enter name of books to del or add
                    print("Enter Name of Book : ") if (books != 0) else ""
                    book_list = []
                    for i in range(books):
                        book_list.append((input(f"{i+1}. ")).strip().title())
                    
                    #For add book
                    if(dashboard_user == "2"):
                        print(" -->", colored(globals()[library].addBooks(book_list), 'green'))
                    #For delete book
                    else:
                        
                        print(" -->", colored(globals()[library].delBooks(book_list), 'magenta'))

            #Invalid Input [next iteation of w-loop-2]
            elif(dashboard_user != "4"):
                print(colored("INVALID INPUT".center(100, "-"), 'red'))
                
            else:
                #[end of w-loop-2]
                break 
        break #[direct end of w-loop-1]   

    #Invalid Input [next iteation of w-loop-1]
    elif(user != "1" and user != "2"):
        print(colored("------>  INVALID INPUT", 'red'))
    
    #Quit [end of w-loop-1]
    else:
        break

#END
print("     THANKS TO VISIT     ".center(100, "-"))
    

     


