#create a dictionary to store student`s data
students={'std01':'Rahul','std02':'Priya','std03':'Amit','std04':'Sneha','std05':'Rohan'}
#to display all student`s data
print("Student details:")
print("---------------------------------")
#to update record of student whose roll number is std103
students['std03']='Amit Kumar'
print("Student details after updation:")
print(students)
print("---------------------------------")
#to delete record of student whose roll number is std104
del students['std04']
print("Student details after deletion:")
print(students)
print("---------------------------------")
# to display all student`s data
for key,value in students.items():
    print(key,value) 
print("---------------------------------")
    