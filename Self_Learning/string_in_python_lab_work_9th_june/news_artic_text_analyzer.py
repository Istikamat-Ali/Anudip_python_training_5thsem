'''Assignment 5: News Article Text Analyzer 
Problem Statement 
A news agency wants to analyze the content of an article. 
Use a paragraph containing at least 300 words. 
Requirements 
1. Count total characters.  
2. Count total words.  
3. Count total sentences.  
4. Count vowels and consonants.  
5. Find longest word.  
6. Find shortest word.  
7. Find the most frequent word.  
8. Create a dictionary of word frequencies.  
9. Display words appearing only once.  
10. Display words appearing more than 5 times.  
11. Count words starting with each alphabet.  
12. Display all unique words.  
Challenge 
Generate a complete text summary: 
Total Words 
Total Sentences 
Average Word Length 
Most Frequent Word 
Vocabulary Size'''
print("---------------------News Article Text Analyzer--------------------")
#taking input from user
text = input("Enter a paragraph containing at least 300 words: ").strip()
print("-------------------------------------------------------------")
#counting total characters
total_characters = len(text)
print(f"Total Characters : {total_characters}")
print("-------------------------------------------------------------")
#splitting words
words = text.split()
#counting total words
total_words = len(words)
print(f"Total Words : {total_words}")
print("-------------------------------------------------------------")
#counting total sentences
sentences = text.split(".")
total_sentences = len(sentences)
print(f"Total Sentences : {total_sentences}")
print("-------------------------------------------------------------")
#counting vowels and consonants
vowels = 0
consonants = 0
for char in text:
    if char.isalpha():
        if char.lower() in "aeiou":#for calculating vowels after converting to lowercase
            vowels += 1
        else:
            consonants += 1
print(f"Vowels : {vowels}")
print(f"Consonants : {consonants}")
print("-------------------------------------------------------------")
#finding longest word
longest_word_length = len(words[0])
for word in words:
    if len(word) > longest_word_length:
        longest_word = word
        longest_word_length = len(word)
print(f"Longest Word : {longest_word} , Length : {longest_word_length}")
print("-------------------------------------------------------------")
#finding shortest word
shortest_word_length = len(words[0])
for word in words:
    if len(word) < shortest_word_length:
        shortest_word = word
        shortest_word_length = len(word)
print(f"Shortest Word : {shortest_word} , Length : {shortest_word_length}")
print("-------------------------------------------------------------")
#finding most frequent word
word_freq = {}
#creating a dictionary of word frequencies and counting word frequencies
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
#finding most frequent word
for word, freq in word_freq.items():
    if freq == max(word_freq.values()):
        most_freq_word = word
print(f"Most Frequent Word : {most_freq_word}")
print("-------------------------------------------------------------")
#displaying words appearing only once
for word in words:
    if word_freq[word] == 1:
        print(word)
print("-------------------------------------------------------------")
#displaying words appearing more than 5 times
for word in words:
    if word_freq[word] > 5:
        print(word)
print("-------------------------------------------------------------")
#counting words starting with each alphabet
word_starts = {}
for word in words:
    if word[0] in word_starts:
        word_starts[word[0]] += 1
    else:
        word_starts[word[0]] = 1
print("Words Starting with Each Alphabet:")
for letter, count in word_starts.items():
    print(f"{letter} : {count}")
print("-------------------------------------------------------------")
#displaying all unique words
unique_words = set(words)
print("Unique Words:")
for word in unique_words:
    print(word)
print("-------------------------------------------------------------")
print("Challenge : Generate a complete text summary:")
print("Total Words:", total_words)
print("Total Sentences:", total_sentences)
print("Average Word Length:", total_characters / total_words)#average word length is the total number of characters divided by the total number of words
print("Most Frequent Word:", most_freq_word)
print("Vocabulary Size:", len(unique_words))#vocabulary size is the number of unique words
print("-------------------------------------------------------------")
