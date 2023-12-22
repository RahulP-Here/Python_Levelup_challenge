''' EXERCISE - 8 : ! CLEAR THE CLUTTER !'''

from termcolor import colored #Termcolor : coloring font in Terminal 
from FolderClass import *
      
#------------ USER DASHBOARD -------------      

#Create Object of Folder class
print("")
path = input('Enter Path of Folder: ')
f = Folder(path)

loading(1)

while(True):
    print(colored("\nPress >>>", 'light_yellow'))
    print(colored("    1. Clear Clutter\n    2. Show All Files\n    3. Show Specific Format Files\n    4. Exit\n", 'light_yellow'))
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

# D:\Github\Levelup_Challange\Level_8\Clutter


     


