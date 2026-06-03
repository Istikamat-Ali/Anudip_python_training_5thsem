#program to convert time into corresponding hour,minute and second
#input of time in second
second=int(input("Enter the time in second: "))
#check second is negative 
if(second<0):
    exit("Time cannot be negative .... Exited")
#----------------------------------------------------
hour=0
minute=0
sec=second
#convert second into hour
if(second>=3600):
    hour=second//3600
    second=second%3600
#------------------------------------------------
#convert second into minute
if(second>=60):
    minute=second//60
    second=second%60
#------------------------------------------------

print("---------------------------------------------")
print("User Input Time : ", sec, "seconds")
#Display time in hour, minute and second
print("---------------------------------------------")
print("Equivalent Time : ", hour, "hour", minute, "minute", second, "second")

