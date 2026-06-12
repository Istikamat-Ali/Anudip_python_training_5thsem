'''Write a program to copy entire content from one file into another file.'''
#reading source file
source_file = input("Enter Source File Name: ")
destination_file = input("Enter Destination File Name: ")
with open(source_file, "r") as source:
    content = source.read()
with open(destination_file, "w") as destination:
    destination.write(content)
print("File copied successfully.")