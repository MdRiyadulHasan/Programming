from collections import Counter

# Create a Counter object
word_count = Counter({'apple': 5, 'banana': 3, 'cherry': 2})

# Get the most common element
most_common_element = word_count.most_common(2)[1][0]
print(most_common_element)
