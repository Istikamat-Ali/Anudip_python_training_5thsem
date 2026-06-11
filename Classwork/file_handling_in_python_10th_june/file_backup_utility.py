'''Problem Statement 2: File Backup Utility 
An organization wants to create backups of important text files to prevent accidental data loss. You have been 
asked to develop a utility that creates an exact copy of an existing file. 
Requirements 
Write a Python program that reads the entire contents of a source file and copies them into another 
destination file. 
The program should: 
1. Accept the names of the source file and destination file from the user.  
2. Read the complete contents of the source file.  
3. Write the contents into the destination file.  
4. Display a success message after the copying process is completed.  
Sample Source File (notes.txt) 
Functions help in code reusability. 
File handling enables persistent storage. 
Python provides various modes to work with files. 
Expected Output 
Enter Source File Name      : notes.txt 
Enter Destination File Name : backup.txt 
 
File copied successfully. 
All contents from 'notes.txt' have been copied to 'backup.txt'. '''
print("---------------------File Backup Utility---------------------")
#reading source file
source_file = input("Enter Source File Name: ")
destination_file = input("Enter Destination File Name: ")
with open(source_file, "r") as source:
    content = source.read()
with open(destination_file, "w") as destination:
    destination.write(content)
print("File copied successfully.")
print("All contents from '{}' have been copied to '{}'.".format(source_file, destination_file))
