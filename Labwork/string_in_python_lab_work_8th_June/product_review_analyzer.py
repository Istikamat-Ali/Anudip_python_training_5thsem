'''5. Product Review Analyzer
Problem Statement
A customer submits a review:
This product is excellent excellent excellent and very useful
Tasks
Write a program to:
1. Count total words. 
2. Create a dictionary containing word frequencies. 
3. Find the most frequently used word. 
4. Find all words appearing only once. 
5. Count words having more than 5 characters. 
6. Display words in reverse order. 
7. Create a list of unique words. 
Sample Output
Total Words: 8
Word Frequencies:
This -> 1
product -> 1
is -> 1
excellent -> 3
and -> 1
very -> 1
useful -> 1
Most Frequent Word: excellent
Words Appearing Once:
['This', 'product', 'is', 'and', 'very', 'useful']
Unique Words:
['This', 'product', 'is', 'excellent', 'and', 'very', 'useful']'''
print("---------------------Product Review Analyzer---------------------")
# review submitted by a customer
review = "This product is excellent and very useful"
print("Review:\n", review)
print("---------------------------------------------------------------------------------")
# counting the total number of words
total_words = len(review.split())
print("Total Words:", total_words)
print("---------------------------------------------------------------------------------")
# creating a dictionary to store word frequencies
word_freq = {}
for word in review.split():#split() method is used to split the string into individual words of list
    if word in word_freq:
        word_freq[word] += 1#update the frequency of the word in dictionary
    else:
        word_freq[word] = 1
print("Word Frequencies:")
for word, freq in word_freq.items():
    print(word, "->", freq)
print("---------------------------------------------------------------------------------")
# finding the most frequently used word
most_freq_word = max(word_freq, key=word_freq.get)#max(dict, key) method is used to find the key with maximum value
print("Most Frequent Word:", most_freq_word)
print("---------------------------------------------------------------------------------")
# finding words appearing only once
unique_words = [word for word in word_freq if word_freq[word] == 1]#list comprehension for finding unique words
print("Words Appearing Once:")
print(unique_words)
print("---------------------------------------------------------------------------------")
'''# counting words having more than 5 characters
long_words = [word for word in review.split() if len(word) > 5]
print("Words Longer Than 5 Characters:")
print(long_words)
print("---------------------------------------------------------------------------------")
# displaying words in reverse order
reverse_words = review.split()[::-1]
print("Words in Reverse Order:")
print(reverse_words)
print("---------------------------------------------------------------------------------")'''
# creating a list of unique words
unique_words = list(set(review.split()))#set() method is used to create a set of unique words and convert it to a list
print("Unique Words:")
print(unique_words)
print("---------------------------------------------------------------------------------")