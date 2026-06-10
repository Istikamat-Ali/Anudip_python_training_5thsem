'''Assignment 3: Chat Message Analytics Dashboard 
Problem Statement 
A messaging application wants to analyze chat messages. 
Store at least 20 chat messages in a list. 
Requirements 
For each message: 
1. Count total words.  
2. Count total characters.  
3. Count vowels and consonants.  
4. Find longest word.  
5. Find shortest word.  
6. Count occurrence of each word.  
7. Display repeated words.  
8. Display words starting with vowels.  
9. Display words longer than 5 characters.  
10. Create a dictionary containing word frequencies.  
Challenge 
Generate a report showing: 
Most Frequently Used Word 
Longest Message 
Shortest Message 
Average Words Per Message'''
#===============================================================================
#                    CHAT MESSAGE ANALYTICS DASHBOARD
#===============================================================================
print("---------------------Chat Message Analytics Dashboard--------------------")
#creating empty list
chat_messages = []
#taking input from user for chat messages
while len(chat_messages) < 20:
    message = input("Enter Chat Message:  ").strip()
    chat_messages.append(message)
print("---------------------------------------------------------------------------")
print("1.Total words in each message :")
#using for loop to print total words in each message
for message in chat_messages:
    words = message.split()
    total_words = len(words)
#displaying total words
    print("Message :", message)
    print("Total Words :", total_words)
    print()
print("---------------------------------------------------------------------------")   
print("\n2.Total characters in each message")
#for loop to print total characters
for message in chat_messages:
    total_characters = len(message)
#printing total characters
    print(f"Message : {message}")
    print(f"Total Characters : {total_characters}")
    print()
print("---------------------------------------------------------------------------")
print("\n3.Vowels  and Consonants in each message")
#for loop to print vowels and consonants
for message in chat_messages:
#initializing variables
    vowels = 0
    consonants = 0
#using for loop
    for char in message:
        if char.isalpha():
            if char.lower() in "aeiou":#for calculating vowels
                vowels += 1
            else:
                consonants += 1
#printing vowels and consonants
    print(f"Message : {message}")
    print(f"Vowels : {vowels}")
    print(f"Consonants : {consonants}")
    print()
print("---------------------------------------------------------------------------")
print("\n4. longest word in each message")
#for loop to print longest word
for message in chat_messages:
    #splitting words in each message
    words = message.split()
    for word in words:
        longest_word = max(words, key=len)#max function to find longest word and key is a function that returns the length of each word
    #displaying longest word
        print(f"Message : {message}")
        print(f"Longest Word : {longest_word}")
        print()
print("---------------------------------------------------------------------------")
print("\n5. Shortest Word in Each Message")
#for loop to print shortest word
for message in chat_messages:
#splitting words
    words = message.split()
#using min function to find shortest word
    for word in words:
        shortest_word = min(words, key=len)
#displaying shortest word
        print(f"Message : {message}")
        print(f"Shortest Word : {shortest_word}")
        print()
print("---------------------------------------------------------------------------")
print("\n6. Word occurences in each message:")
#for loop to print word occurences
for message in chat_messages:
    #creating empty dictionary
    word_count = {}
    #splitting words and converting to lowercase
    words = message.lower().split()
    #using for loop to count word occurences
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
#displaying each message and word occurences
    print(f"Message : {message}")
#printing word occurences
    for word, count in word_count.items():
        print(f"{word} --> {count}")
    print()
print("---------------------------------------------------------------------------")
print("\n7.Repeated Words in Each Message:")
#for loop to print repeated words
for message in chat_messages:
#creating empty dictionary for repeated words
    repeated_words = {}
#splitting words and converting to lowercase
    words = message.lower().split()
#using for loop to count repeated words
    for word in words:
#if word is in repeated words
        if word in repeated_words:
            repeated_words[word] += 1
        else:
            repeated_words[word] = 1
#displaying each message and repeated words
    print(f"Message : {message}")
    #flag variable to check if repeated words are found
    found = False
    #using for loop to print repeated words
    for word, count in repeated_words.items():
        #if count is greater than 1
        if count > 1:
            print(f"{word} --> {count} times")
            found = True# setting flag variable to True
    #if no repeated words are found
    if not found:
        print("No Repeated Words Found")
#displaying empty line
    print()
print("---------------------------------------------------------------------------")
print("\n8. Words Starting With Vowels")
# for loop to print words starting with vowels
for message in chat_messages:
#splitting words
    words = message.split()
#displaying each message
    print(f"Message : {message}")
#flag variable to check if words starting with vowels are found
    found = False
#using for loop to print words starting with vowels
    for word in words:
        if word[0].lower() in "aeiou":#if first character of word is a vowel
            print(word)
            found = True#setting flag variable to True 
    #if no words starting with vowels are found
    if not found:
        print("No Word Starts With a Vowel")
    #displaying empty line
    print()
print("---------------------------------------------------------------------------")
print("\n9. Word Longer Than 5 Characters")
# for loop to print words longer than 5 characters
for message in chat_messages:
#splitting words
    words = message.split()
#displaying each message
    print(f"Message : {message}")
#flag variable to check if words longer than 5 characters are found
    found = False
#using for loop to print words longer than 5 characters
    for word in words:
#if length of word is greater than 5
        if len(word) > 5:
            print(word)
            found = True
#if no words longer than 5 characters are found
    if not found:
        print("No Word Longer Than 5 Characters")
#displaying empty line
    print()
print("---------------------------------------------------------------------------")
print("\n10. Word Frequency in Each Message:")
#for loop to print word frequency
for message in chat_messages:
#creating empty dictionary
    word_frequency = {}
#splitting words and converting to lowercase
    words = message.lower().split()
#using for loop to count word frequency
    for word in words:
#if word is in word frequency
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
#displaying each message and word frequency
    print(f"Message : {message}")
    print(word_frequency)
    print()
print("---------------------------------------------------------------------------")
print("CHALLENGE REPORT")
print("---------------------------------------------------------------------------")
# Dictionary to store overall word frequencies
overall_frequency = {}
# Variable to count total words from all messages
total_words_all_messages = 0
#for loop to count total words and word frequencies
for message in chat_messages:
#splitting words
    words = message.split()
#counting total words for all messages
    total_words_all_messages += len(words)
#for loop to count word frequencies
    for word in words:
#if word is in overall frequency
        if word in overall_frequency:
            overall_frequency[word] += 1
        else:
            overall_frequency[word] = 1
print("-----------------------------------------------------------------------")
print("\nMost Frequently Used Word")
#initialising variables to find most frequently used word
most_used_word = ""
highest_count = 0
#using for loop to find most frequently used word
for word in overall_frequency:
    if overall_frequency[word] > highest_count:
        highest_count = overall_frequency[word]
        most_used_word = word

print("Most Frequently Used Word :", most_used_word)
print("Frequency :", highest_count)
print("-----------------------------------------------------------------------")
print("Longest Message:")
longest_message = ""
for message in chat_messages:
    if len(message) > len(longest_message):
        longest_message = message
print(f"Message : {longest_message}")
print(f"Length : {len(longest_message)}")
print("-----------------------------------------------------------------------")
print("Shortest Message:")
shortest_message = chat_messages[0]
for message in chat_messages:
    if len(message) < len(shortest_message):
        shortest_message = message
print(f"Message : {shortest_message}")
print(f"Length : {len(shortest_message)}")
print("-----------------------------------------------------------------------")
print("Average Words Per Message:")
average_words = total_words_all_messages / len(chat_messages)
print(f"Average : {round(average_words, 2)}")
print("-----------------------------------------------------------------------")
