''' EXERCISE - 8 : ! FOLDER CLASS !'''

#For Class
import os
import asyncio
from termcolor import colored #Termcolor : coloring font in Terminal 

#For Loading Animation
import sys
import time

#------------ FOLDER CLASS -------------      
class Folder:
    #Initialize The Folder Object
    def __init__(self, path):
        self.path = path

        try:
            self.files = os.listdir(self.path)
            self.name = list(path.split('\\'))[(len(list(path.split('\\')))) - 1]
        except Exception as e:
            print(colored(f"Error ! {e}", 'red'))
            exit()

        loading(5)
        print(colored(f"\n----> {self.name} has been successfully switch into Operation Mode !", 'green'))
    
    #clear clutter by renaming files
    def clearClutter(self, Extension, name):
        self.list = []
        if(('.' in Extension) == False):
            Extension = '.' + Extension

        for file in self.files:
            if file.endswith(Extension):
                self.list.append(file)
        try:
            for index,file in enumerate(self.list):

                old = f"{self.path}\{file}"
                new = f"{self.path}\\{name}_{index+1}{Extension}"

                os.rename(old, new)

            if(len(self.list) != 0):
                print(colored("\n----> Clutter Cleared Successfully !", 'green'))
            else:
                print(colored(f"There is not {Extension} file in {self.name} Folder !", 'red'))

        except Exception as e:
            print(e)

        self.files = os.listdir(self.path)
    
    #display files with a specific extension
    def showFiles(self, Extension):
        i = 0
        for file in self.files:
            if file.endswith(Extension):
                print(f"    > {i+1}. {file}")
                i = i+1
        if(i == 0):
            print(colored(f"There is not {Extension} file in {self.name} Folder !", 'red'))

    #display all files in the folder
    def showAllFiles(self):
        for index,file in enumerate(self.files):
            print(f"    > {index+1}. {file}")

        if(len(self.files) == 0):
            print(colored(f"{self.name} is an EMpty Folder !", 'red'))


#------------ LOADING ANIMATION -------------
def loading(n):
    i = 0
    while i < n:
        sys.stdout.write(colored('\r.... LOADING .   ', 'yellow'))
        time.sleep(0.1)
        sys.stdout.write(colored('\r.... LOADING ..  ', 'yellow'))
        time.sleep(0.1)
        sys.stdout.write(colored('\r.... LOADING ... ', 'yellow'))
        time.sleep(0.1)
        sys.stdout.write(colored('\r.... LOADING ....', 'yellow'))
        time.sleep(0.1)
        i = i+1
    sys.stdout.write('\r                      ')