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
    for line in file:
        print(line.strip())
        #p_id,p_name,p_status=line.strip().split(",")#splitting line by comma in a list
        #print(p_id,p_name,p_status)
#display critical patients
print("Critical Patients:")
with open("patients.txt","r") as file:
    for line in file:
        p_id,p_name,p_status=line.strip().split(",")#splitting line by comma in a list
        if "Critical" in file:
            print(p_name)
#count patients under each status
print("Patient Count:")
with open("patients.txt","r") as file:
    normal_count=0
    stable_count=0
    critical_count=0
    for f in file:
        p_id,p_name,p_status=f.strip().split(",")
        if "Normal" in f:
            normal_count+=1
        elif "Stable" in f:
            stable_count+=1
        elif "Critical" in f:
            critical_count+=1
    print("Normal:",normal_count)
    print("Stable:",stable_count)
    print("Critical:",critical_count)
#search patient details using Patient ID
patient_id=input("Enter Patient ID to search:")
with open("patients.txt","r") as file:
    for line in file:
        p_id,p_name,p_status=line.strip().split(",")
        if patient_id==p_id:
            print("Patient Found:")
            print(line.strip())
            break
        else:
            print("Patient not found.")
#save critical patient records to critical_patients.txt
with open("patients.txt","r") as file:
    for line in file:
        if "Critical" in line:
            with open("critical_patients.txt","a") as f:
                f.write(line)
print("Critical Patient Report Generated Successfully.")