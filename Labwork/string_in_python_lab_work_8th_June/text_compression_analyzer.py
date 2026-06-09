'''10. Text Compression Analyzer
Problem Statement
A compressed message is given:
AAABBBCCCDDDAAA
Tasks
Write a program to:
1. Count occurrences of each character. 
2. Create a dictionary of character frequencies. 
3. Display unique characters. 
4. Find the most frequent character. 
5. Create a compressed output: 
A3B3C3D3A3
6. Calculate compression ratio. 
Sample Output
Original Text:
AAABBBCCCDDDAAA
Character Frequencies:
A -> 6
B -> 3
C -> 3
D -> 3
Unique Characters:
['A', 'B', 'C', 'D']
Most Frequent Character: A
Compressed Output:
A3B3C3D3A3
Original Length: 15
Compressed Length: 10
Compression Ratio: 66.67%'''
print("---------------------Text Compression Analyzer---------------------")
#compressed message
message = "AAABBBCCCDDDAAA"
print("Original Text:")
print(message)
print("-------------------------------------------------------------")
#counting the occurrences of each character
char_freq = {}
for char in message:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
#creating a dictionary of character frequencies
print("Character Frequencies:")
for char, count in char_freq.items():
    print(char, "->", count)
print("-------------------------------------------------------------")
#displaying unique characters
unique_chars = list(char_freq.keys())
print("Unique Characters:")
print(unique_chars)
print("-------------------------------------------------------------")
#finding the most frequent character
most_frequent_char = max(char_freq, key=char_freq.get)#max(dict, key) method is used to find the key with maximum value
print("Most Frequent Character:", most_frequent_char)
print("-------------------------------------------------------------")
#creating a compressed output
compressed_output = most_frequent_char + str(char_freq[most_frequent_char])
for char in unique_chars:
    if char != most_frequent_char:
        compressed_output += char + str(char_freq[char])
print("Compressed Output:")
print(compressed_output)
print("-------------------------------------------------------------")
#calculating the compression ratio
original_length = len(message)
compressed_length = len(compressed_output)#compressed_length is the length of the compressed output
compression_ratio = (compressed_length / original_length) * 100#compression_ratio is calc by dividing compressed_length by original_length
print("Original Length:", original_length)
print("Compressed Length:", compressed_length)
print("Compression Ratio:", compression_ratio, "%")
print("-------------------------------------------------------------")