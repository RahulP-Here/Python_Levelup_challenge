''' EXERCISE - 6 : ! PDF MERGER !'''

import pypdf as p

#PDF MERGER
def merge(files):

    #Create a Object of PDF Writer
    merger = p.PdfWriter()

    lst = list(files)
    for pdf in lst:

        try:
            merger.append(pdf) #add pdf content in writer
        except Exception as e:
            print(e)

    #Create Final PDF File
    File_location = input("Enter Location where file will store : ")
    mergedFile_name = input("Enter new pdf Name : ") + ".pdf" 

    #Write content into new file
    merger.write(f"{File_location}/{mergedFile_name}") #write content into new file

    #Disable PDF Writer
    merger.close()

    #For User Referance
    new_file_location = f"! SUCCESS ! Your pdf saved at {File_location}/{mergedFile_name}"
    print(new_file_location)

    return new_file_location

#-------------------------------------

#Input PDF Files
pdf_files = []

for i in range(int(input("How Many pdf need to merge : "))):
    file = input("Enter File name include location : ")
    pdf_files.append(file)
print("---------------------------------------\n")
#Merge PDf Files
merge(pdf_files)
