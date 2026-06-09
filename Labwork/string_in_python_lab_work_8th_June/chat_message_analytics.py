'''3. Chat Message Analytics
Problem Statement
A chat application stores a message:
Python is awesome and Python is easy to learn
Tasks
Write a program to:
1. Count total characters. 
2. Count total words. 
3. Find the longest word. 
4. Find the shortest word. 
5. Count how many times the word "Python" appears. 
6. Create a list of words having more than 4 characters. 
7. Display all words starting with a vowel. 
8. Count the number of vowels and consonants. 
Sample Output
Message:
Python is awesome and Python is easy to learn
Total Characters: 45
Total Words: 8
Longest Word: awesome
Shortest Word: is
Occurrences of Python: 2
Words Longer Than 4 Characters:
['Python', 'awesome', 'Python', 'learn']
Vowels: 16
Consonants: 22'''
print("---------------------Chat Message Analytics---------------------")
# message stored in chat application
message = "Python is awesome and Python is easy to learn"
print("Message:\n", message)
print("---------------------------------------------------------------------------------")
# counting total characters
total_characters = len(message)
print("Total Characters:", total_characters)
print("---------------------------------------------------------------------------------")
# counting total words
total_words = len(message.split())#split() method is used to split the string into a list of words
print("Total Words:", total_words)
print("---------------------------------------------------------------------------------")
# finding the longest word
longest_word = max(message.split(), key=len)#max(list, key) method is used to find the longest word , key is a function that returns the length of each word
print("Longest Word:", longest_word)
print("---------------------------------------------------------------------------------")
# finding the shortest word
shortest_word = min(message.split(), key=len)
print("Shortest Word:", shortest_word)
print("---------------------------------------------------------------------------------")
# counting the number of times the word "Python" appears
python_count = message.count("Python")
print("Occurrences of Python:", python_count)
print("---------------------------------------------------------------------------------")
# creating a list of words having more than 4 characters
four_char_words = [word for word in message.split() if len(word) > 4]#list comprehension for finding words having more than 4 characters
print("Words Longer Than 4 Characters:")
print(four_char_words)
print("---------------------------------------------------------------------------------")
# displaying all words starting with a vowel
vowel_words = [word for word in message.split() if word[0] in "aeiouAEIOU"]
print("Vowels:")
print(vowel_words)
print("---------------------------------------------------------------------------------")
# counting the number of vowels and consonants
vowels = sum(1 for char in message if char in "aeiouAEIOU")
consonants = sum(1 for char in message if char not in "aeiouAEIOU")
print("Vowels:", vowels)
print("Consonants:", consonants)
print("---------------------------------------------------------------------------------")