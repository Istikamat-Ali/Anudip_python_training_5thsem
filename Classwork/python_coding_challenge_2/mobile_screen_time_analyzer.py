'''Problem 5: Mobile Screen Time Analyzer 
Problem Statement 
Daily mobile screen time (in minutes) of a student is recorded for 10 days. 
Sample Data 
screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260] 
Tasks 
1. Calculate average screen time.  
2. Find the highest and lowest screen time.  
3. Count days exceeding 200 minutes.  
4. Display days with healthy usage (<180 minutes).  
5. Categorize usage:  
o Healthy (<180)  
o Moderate (180–240)  
o Excessive (>240)  
Sample Output 
Average Screen Time: 205.5 minutes 
 
Highest Screen Time: 300 minutes 
 
Lowest Screen Time: 120 minutes 
 
Days Exceeding 200 Minutes: 5 
 
Healthy Usage Days: 
Day 3 
Day 5 
Day 9 
 
Healthy: 3 
Moderate: 4 
Excessive: 3 '''
#given data in list
screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260]
#calculate average screen time
average_screen_time = sum(screen_time) / len(screen_time) #sum of list/length of list
print("Average Screen Time:", average_screen_time)
print()
#find the highest and lowest screen time
highest_screen_time = max(screen_time)
lowest_screen_time = min(screen_time)
print("Highest Screen Time:", highest_screen_time)
print("Lowest Screen Time:", lowest_screen_time)
print()
#count days exceeding 200 minutes
exceeding_200_minutes = sum(1 for time in screen_time if time > 200)
print("Days Exceeding 200 Minutes:", exceeding_200_minutes)
print()
#display days with healthy usage
print("Healthy Usage Days:")
healthy_usage_days =0
for time in screen_time:
    if time < 180:
        print("Day",screen_time.index(time)+1)
print()
#categorizing usage
healthy_usage_days = sum(1 for time in screen_time if time < 180) #generator expression is used to count the number of days
moderate_usage_days = sum(1 for time in screen_time if 180 <= time <= 240)
excessive_usage_days = sum(1 for time in screen_time if time > 240)
print("Healthy:", healthy_usage_days)
print("Moderate:", moderate_usage_days)
print("Excessive:", excessive_usage_days)

