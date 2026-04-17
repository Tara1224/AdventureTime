import nltk
from nltk.tokenize import word_tokenize

# only needed the first time
nltk.download('punkt')

def average_word_length(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    
    words = word_tokenize(text)
    
    # keep only actual words (no punctuation)
    words = [word for word in words if word.isalpha()]
    
    if len(words) == 0:
        return 0
    
    avg = sum(len(word) for word in words) / len(words)
    return avg

def longest_word(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    
    words = word_tokenize(text)
    words = [word for word in words if word.isalpha()]
    
    if not words:
        return ""
    
    return max(words, key=len)

print("Adventure Time Episodes by Average Word Length")
print("Episode 1:", average_word_length("ATE1.txt"), "longest word:", longest_word("ATE1.txt"))
print("Episode 2:", average_word_length("ATE2.txt"), "longest word:", longest_word("ATE2.txt"))
print("Episode 3:", average_word_length("ATE3.txt"), "longest word:", longest_word("ATE3.txt"))
print("Episode 4:", average_word_length("ATE4.txt"), "longest word:", longest_word("ATE4.txt"))
print("Episode 5:", average_word_length("ATE5.txt"), "longest word:", longest_word("ATE5.txt"))
print("Episode 6:", average_word_length("ATE6.txt"), "longest word:", longest_word("ATE6.txt"))
print("Episode 7:", average_word_length("ATE7.txt"), "longest word:", longest_word("ATE7.txt"))
print("Episode 8:", average_word_length("ATE8.txt"), "longest word:", longest_word("ATE8.txt"))
print("Episode 9:", average_word_length("ATE9.txt"), "longest word:", longest_word("ATE9.txt"))
print("Episode 10:", average_word_length("ATE10.txt"), "longest word:", longest_word("ATE10.txt"))
print("Episode 11:", average_word_length("ATE11.txt"), "longest word:", longest_word("ATE11.txt"))
print("Episode 12:", average_word_length("ATE12.txt"), "longest word:", longest_word("ATE12.txt"))
print("Episode 13:", average_word_length("ATE13.txt"), "longest word:", longest_word("ATE13.txt"))
print("Episode 14:", average_word_length("ATE14.txt"), "longest word:", longest_word("ATE14.txt"))
print("Episode 15:", average_word_length("ATE15.txt"), "longest word:", longest_word("ATE15.txt"))
print("Episode 16:", average_word_length("ATE16.txt"), "longest word:", longest_word("ATE16.txt"))
print("Episode 17:", average_word_length("ATE17.txt"), "longest word:", longest_word("ATE17.txt"))
print("Episode 18:", average_word_length("ATE18.txt"), "longest word:", longest_word("ATE18.txt"))
print("Episode 19:", average_word_length("ATE19.txt"), "longest word:", longest_word("ATE19.txt"))
print("Episode 20:", average_word_length("ATE20.txt"), "longest word:", longest_word("ATE20.txt"))
print("Episode 21:", average_word_length("ATE21.txt"), "longest word:", longest_word("ATE21.txt"))
print("Episode 22:", average_word_length("ATE22.txt"), "longest word:", longest_word("ATE22.txt"))
print("Episode 23:", average_word_length("ATE23.txt"), "longest word:", longest_word("ATE23.txt"))
print("Episode 24:", average_word_length("ATE24.txt"), "longest word:", longest_word("ATE24.txt"))
print("Episode 25:", average_word_length("ATE25.txt"), "longest word:", longest_word("ATE25.txt"))
print("Episode 26:", average_word_length("ATE26.txt"), "longest word:", longest_word("ATE26.txt"))
print("All files analyzed!")