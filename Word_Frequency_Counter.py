import string

def count_words(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.lower().split()
    
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    return word_counts

paragraph = "Python is amazing. Python is fast, and learning Python is fun!"
result = count_words(paragraph)

print("Word Counts:")
for word, count in result.items():
    print(f"{word}: {count}")
