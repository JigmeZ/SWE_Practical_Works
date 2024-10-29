def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def count_lines(content):
    return len(content.split('\n'))

def count_words(content):
    return len(content.split())

from collections import Counter
def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def count_unique_words(content):
    words = content.lower().split()
    unique = set(words)
    return len(unique)

def longest_word(content):
    words = content.split()
    return max(words, key=len)

## def count_specific_word(content=None, specific_word= None, filename =  None):
    if filename and not content:  
        with open(filename, 'r') as file:
            content = file.read()
            
    if content and specific_word:  
        words = content.lower().split()
        return words.count(specific_word.lower())
    else:
        return "Please provide specific_word."

def percentage_longer_than_average(content):
    words = content.split()
    avg_length = average_word_length(content)
    longer_than_average = [word for word in words if len(word) > avg_length]
    percentage = (len(longer_than_average) / len(words)) * 100 if words else 0
    return percentage

def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    count = count_unique_words(content)
    longest = longest_word(content)
    longer_avg_word = percentage_longer_than_average(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Unique words: {count}")
    print(f"Longest word: {longest}")
    print(f"Percentage of words longer than average: {longer_avg_word:.2f}%")
    
analyze_text('sample.txt')