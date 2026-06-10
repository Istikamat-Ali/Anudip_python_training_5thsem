'''Assignment 6: Student Resume Analyzer 
Problem Statement 
A student enters a resume as plain text (Name, Skills, Education, Projects, Achievements). 
The system should: 
1. Count total words.  
2. Count total characters.  
3. Extract email IDs.  
4. Extract phone numbers.  
5. Count skills mentioned.  
6. Find repeated keywords.  
7. Identify the most frequently used word.  
8. Generate a skill frequency report.  
9. Detect duplicate skills.  
10. Create a summary dashboard.  
Expected Output 
Resume Analysis Report 
 
Total Words: 420 
Total Characters: 2650 
 
Email Found: 1 
Phone Numbers Found: 1 
 
Most Frequent Skill: Python 
 
Top 5 Keywords: 
Python 
SQL 
React 
Java 
Communication '''
print("---------------------Student Resume Analyzer---------------------")
#taking input from user
resume = input("Enter a resume as plain text (Name, Skills, Education, Projects, Achievements): ").strip()
print("-------------------------------------------------------------")
#counting total words
total_words = len(resume.split())
#counting total characters
total_characters = len(resume)
print()
print("-------------------------------------------------------------")
#extracting email ids
email_ids = []
for word in resume.split():
    if "@" in word:
        email_ids.append(word)
#extracting phone numbers
phone_numbers = []
for word in resume.split():
    if word.isdigit() and len(word) == 10:
        phone_numbers.append(word)
print()
print("-------------------------------------------------------------")
#counting skills mentioned
skills = []
for word in resume.split():
    if word.isalpha():
        skills.append(word)
print("-------------------------------------------------------------")
#finding repeated keywords
repeated_keywords = []
for word in set(skills):
    if skills.count(word) > 1:
        repeated_keywords.append(word)
print("-------------------------------------------------------------")
#finding the most frequently used word
word_freq = {}
for word in skills:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
for word, freq in word_freq.items():
    if freq == max(word_freq.values()):
        most_freq_word = word
print("Most Frequent Skill:", most_freq_word)
print("-------------------------------------------------------------")
#generating skill frequency report
skill_freq = {}
for skill in skills:
    if skill in skill_freq:
        skill_freq[skill] += 1
    else:
        skill_freq[skill] = 1
print("Skill Frequency Report:")
for skill, freq in skill_freq.items():
    print(f"{skill}: {freq}")
print("-------------------------------------------------------------")
#detecting duplicate skills
duplicate_skills = []
for skill, freq in skill_freq.items():
    if freq > 1:
        duplicate_skills.append(skill)
print("Duplicate Skills:", duplicate_skills)
print("-------------------------------------------------------------")
#creating summary dashboard
print("Resume Analysis Report")
print("Total Words:", total_words)
print("Total Characters:", total_characters)
print("Email Found:", len(email_ids))
print("Phone Numbers Found:", len(phone_numbers))
print("Most Frequent Skill:", most_freq_word)
print("Top 5 Keywords:", repeated_keywords)
print("Duplicate Skills:", duplicate_skills)
print("-------------------------------------------------------------")