from collections import defaultdict
import re

# List of sentences
sentences = [
    "This is a test sentence",
    "This sentence is for testing",
    "Test the sentence"
]

# defaultdict with int as the default factory
word_count = defaultdict(int)

# Counting word frequencies
for sentence in sentences:
    words = re.findall(r'\w+', sentence.lower())  # Using regex to split words and converting to lower case
    for word in words:
        word_count[word] += 1

# Printing the word frequencies
for word, count in word_count.items():
    print(f'{word}: {count}')
