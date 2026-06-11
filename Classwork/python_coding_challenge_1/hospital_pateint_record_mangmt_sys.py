'''Problem 2: Hospital Patient Record Management System
Problem Statement
A hospital maintains patient details in a file named patients.txt.
Sample Input/Data (patients.txt)
P101,Anuj,Normal
P102,Rahul,Critical
P103,Priya,Stable
P104,Neha,Critical
P105,Amit,Stable
P106,Sneha,Normal
P107,Karan,Critical
P108,Pooja,Stable
P109,Rohit,Normal
P110,Anjali,Stable
Tasks
1. Display all patient records. 
2. Display critical patients. 
3. Count patients under each status. 
4. Search patient details using Patient ID. 
5. Save critical patient records to critical_patients.txt. 
Sample Output
Critical Patients:
Rahul
Neha
Karan
Patient Count:
Normal : 3
Stable : 4
Critical : 3
Patient Found:
P104,Neha,Critical
Critical Patient Report Generated Successfully.'''
#dispay all patient records
with open("patients.txt","r") as file:
    for file in file.strip().split("    \n"):
        print(file)
#display critical patients
with open("patients.txt","r") as file:
    for file in file.strip().split("\n"):
        if "Critical" in file:
            print(file)
#count patients under each status
with open("patients.txt","r") as file:
    normal_count=0
    stable_count=0
    critical_count=0
    for file in file.strip().split("\n"):
        if "Normal" in file:
            normal_count+=1
        elif "Stable" in file:
            stable_count+=1
        elif "Critical" in file:
            critical_count+=1
    print("Normal:",normal_count)
    print("Stable:",stable_count)
    print("Critical:",critical_count)
#search patient details using Patient ID
with open("patients.txt","r") as file:
    for file in file.strip().split("\n"):
        if "P104" in file:
            print("Patient Found:")
            print(file)
            break
        
#save critical patient records to critical_patients.txt
with open("critical_patients.txt","w") as file:
    for file in file.strip().split("\n"):
        if "Critical" in file:
            file.write(file)
print("Critical Patient Report Generated Successfully.")