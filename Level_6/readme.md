[Scroll Down](#end)

# PYTHON : 10 DAYS LEVEL-UP CHALLANGE [DAY-6]

## 6. PDF MERGER
Congratulations we already completed a half of this challange.

On Day 6 We'll Create a `PDF Merger` in Python. In this Program we create a Dashboard which take Files from the local device as a input and merge them in new created single pdf file, also store new pdf file in local storage.

We have [3 PDF Files](/Level_6/pdf_files/), we'll merge them all into one single pdf file.

![input pdfs](/img/Level6_outpput/input%20pdfs.png)


#### Require Topics :
- [Oop in Python](https://www.geeksforgeeks.org/python-oops-concepts/)
- [Pip installation](https://pypi.org/project/pip/)  
- [Python Pypdf module](https://pypi.org/project/pypdf/)  
- [Exception Handeling](https://www.geeksforgeeks.org/python-exception-handling/)
- [Try... Except... block](https://www.w3schools.com/python/python_try_except.asp)

so here we go...

<br>

---

**Steps :**

- [Install Pypdf](#--install-pypdf-module)
- [Basic Structure](#--basic-structure)
- [Input PDF](#--input-pdf-files)
- [Merge Function](#--merge-function)
- [Output](#output)

---          
- [Logic Template](#logic-template)
---

### - Install Pypdf Module

Install [pypdf](https://pypi.org/project/pypdf/) using pip:

- Open terminal.
- Enter this command : 

```
pip install <package-name>
```

![pypdf intallation](/img/Level6_outpput/pypdf%20intallation.png)

- Installed succesfully.

![pypdf intalled](/img/Level6_outpput/pypdf%20intalled.png)

> Note : [Pip](https://pypi.org/project/pip/) is the standard package manager for Python.It use for installing Python packages and their dependencies in a secure manner.

### - Basic Structure

First we need to import a python module called [pypdf](https://pypi.org/project/pypdf/).

- `import pypdf`

After that, we need to declare a [Function](https://www.w3schools.com/python/python_functions.asp) which merge the pdf and store new file into local storage.
- `def merge(files): `

At Last we'll taking file locations as a input from user and passed them into [merger function](#--merge-function).


```python
    import pypdf

    #PDF MERGER
    def merge(files):
        #merge the files
        #save into local
        return new_file_location

    #Input PDF Files

    #Merge PDf Files
    merge(files)

```

> Note : [pypdf](https://pypi.org/project/pypdf/) is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files.

---

<br>

### - Input PDF Files
For Merging the files, we need ask user to enter the file location for accessing the files.

```python
    pdf_files = []

    for i in range(int(input("How Many pdf need to merge : "))):
        file = input("Enter File name include location : ")
        pdf_files.append(file)
```

- Here we using [for loop](https://www.w3schools.com/python/python_for_loops.asp) for browsing multiple files repeatedly, according how many files user want to merge.

- With each iteration we store the file location in the empty list one by one.
```python
    pdf_files = []
    pdf_files.append(file)
```
> Note : [list.append()](https://www.w3schools.com/python/ref_list_append.asp) method appends an element to the end of the list.

At the end we pass the whole file list to the merge function
```python
    merge(pdf_files)
```

---

<br>
     
### - Merge Function
Now we start code for merge function that...

- 1. Merge all the file's (From the argument list) content into one single pdf file.

```python
    def merge(files):
        #Create a Object of PDF Writer
        merger = pypdf.PdfWriter()

        #Append each pdf content into writer
        merger.append(pdf) #All Pdf Files One by one (use for loop)

        #Write content into new file
        merger.write(new_file)

        merger.close()
```
>Note: [PdfWriter( )](https://pypdf.readthedocs.io/en/stable/modules/PdfWriter.html?highlight=pdfwrite) is class that supports writing PDF files out, given pages produced by another class

- 2. Store the new pdf into local folder via manual browsing.

```python
    def merge(files):
        #Merge pdfs 

        #Create new Pdf 
        File_location = input("Enter Location where file will store : ")
        mergedFile_name = input("Enter new pdf Name : ") + ".pdf" 

        return new_file_location
```

* Here we should use [Try...Except...](https://www.w3schools.com/python/python_try_except.asp) block for hendeling the exception which is produced when entered file is didn't exist or incorrect location / format.

```python
    def merge(files):
        #Create a Object of PDF Writer
        merger = pypdf.PdfWriter()

        #Append each pdf content into writer
        try:
            merger.append(pdf) #All Pdf Files One by one (use for loop)
        except:
            print(exception)

        #Create new Pdf 
        File_location = input("Enter Location where file will store : ")
        mergedFile_name = input("Enter new pdf Name : ") + ".pdf" 
        
        #Write content into new file
        merger.write(new_file)

        merger.close() 


        return new_file_location
```

---

<br>
            
##  Logic Template
```python
    import pypdf

    #PDF MERGER
    def merge(files):
        #Create a Object of PDF Writer
        merger = pypdf.PdfWriter()

        #Append each pdf content into writer
        try:
            merger.append(pdf) #All Pdf Files One by one (use for loop)
        except:
            print(exception)

        #Create new Pdf 
        File_location = input("Enter Location where file will store : ")
        mergedFile_name = input("Enter new pdf Name : ") + ".pdf" 
        
        #Write content into new file
        merger.write(new_file)

        merger.close() 

        return new_file_location

    #Input PDF Files
    pdf_files = []

    for i in range(int(input("How Many pdf need to merge : "))):
        file = input("Enter File name include location : ")
        pdf_files.append(file)

    #Merge PDf Files
    merge(files)
```

---

<br>
     
##  output  
#### Ask For File Location :  
![image](/img/Level6_outpput/ask%20file%20location.png) 

#### Enter File Locations :  
![image](/img//Level6_outpput/input%20file%20locations.png) 

#### Enter Output File Location :  
![image](/img/Level6_outpput/input%20output%20location.png) 

#### Success :  
![image](/img/Level6_outpput/success.png) 

#### Output File :  
![image](/img/Level6_outpput/output.png) 

<br>

###### END


> See You In Level 7 👀....
