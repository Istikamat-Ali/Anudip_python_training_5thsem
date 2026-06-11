'''3. Movie Review Sentiment Analyzer 
Problem Statement 
Movie reviews are stored as follows: 
reviews = [ 
    "excellent movie", 
    "average story", 
    "excellent acting", 
    "poor direction", 
    "excellent visuals", 
    "poor screenplay", 
    "good music", 
    "excellent climax", 
    "average performance", 
    "good cinematography" 
] 
Requirements 
Create the following functions: 
1. count_sentiments(reviews) 
Counts: 
• Excellent  
• Good  
• Average  
• Poor reviews  
2. most_common_word(reviews) 
Returns the most frequently occurring word. 
3. longest_review(reviews) 
Returns the review containing the maximum number of characters. 
4. reviews_with_keyword(reviews, keyword) 
Displays all reviews containing a given keyword. 
Sample Output 
Excellent Reviews: 4 
Good Reviews: 2 
Average Reviews: 2 
Poor Reviews: 2 
 
Most Common Word: 
excellent 
 
Longest Review: 
good cinematography 
 
Reviews containing 'excellent': 
excellent movie 
excellent acting 
excellent visuals 
excellent climax '''
print("---------------------Movie Review Sentiment Analyzer---------------------")
#given list representing movie reviews
reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]
#function to count sentiments
def count_sentiments(reviews):
  excellent_count = 0
  good_count = 0
  average_count = 0
  poor_count = 0
  for review in reviews:
    if "excellent" in review:
      excellent_count += 1
    elif "good" in review:
      good_count += 1
    elif "average" in review:
      average_count += 1
    elif "poor" in review:
      poor_count += 1
  return excellent_count, good_count, average_count, poor_count
#function to find the most common word
def most_common_word(reviews):
  word_freq = {}
  for review in reviews:
    for word in review.split():
      if word in word_freq:
        word_freq[word] += 1
      else:
        word_freq[word] = 1
  for word, freq in word_freq.items():
    if freq == max(word_freq.values()):
      return word                       
#function to find the longest review
def longest_review(reviews):
  longest_review = ""
  for review in reviews:
    if len(review) > len(longest_review):
      longest_review = review
  return longest_review
#function to display reviews containing a given keyword
def reviews_with_keyword(reviews, keyword):
  for review in reviews:
    if keyword in review:
      print(review)
#calling functions
excellent_count, good_count, average_count, poor_count = count_sentiments(reviews)#this method is called as unpacking of tuple
print("Excellent Reviews:", excellent_count)
print("Good Reviews:", good_count)
print("Average Reviews:", average_count)
print("Poor Reviews:", poor_count)
print("---------------------------------------------------------------------------------")
print("Most Common Word:\n", most_common_word(reviews))
print("---------------------------------------------------------------------------------")
print("Longest Review:\n", longest_review(reviews))
print("---------------------------------------------------------------------------------")
print("Reviews containing 'excellent':")
reviews_with_keyword(reviews, "excellent")
print("---------------------------------------------------------------------------------")
