import os
from collections import Counter

# Builds the dictionary
# from typing import Dict, Any
def make_dictionary(corpus):
    return os.listdir(corpus)

def read_corpus(corpus, i):
    return open(os.path.join(corpus, i)).read()

# Frequency count of all characters in a text.
def char_freq_count(text):
    return Counter(ch for ch in text.lower() if ch.isalpha())

# Find all unigrams in a document
def calc_unigram(text):
    text = text.split(' ')
    uni = []
    for w in range(len(text)):
        uni.append(text[w])

    return uni

# Find all bigrams in a document
def calc_bigram(text):
    text = text.split(' ')
    bi = []
    for w in range(len(text) - 1):
        bi.append((text[w], text[w + 1]))

    return bi

# Find all trigrams of each document
def calc_trigram(text):
    text = text.split(' ')
    tri = []
    for w in range(len(text) - 2):
        tri.append((text[w], text[w + 1], text[w + 2]))

    return tri

# Open files
output = open("output.txt", 'w')
cfc = open("char_freq.txt", 'w')
mcf = open('common_word.txt', 'w')
unigram = open('unigram.txt', 'w')
bigram = open('bigram.txt', 'w')
trigram = open('trigram.txt', 'w')

# Set corpus
corpus = "gutenberg-corpus"
dict_gut = make_dictionary(corpus)
output.write("Characters in each file: \n")

words = ""

# Write file headers.
unigram.write("===========================\n")
unigram.write("Unigrams\n")
unigram.write("===========================\n")

bigram.write("===========================\n")
bigram.write("Bigrams\n")
bigram.write("===========================\n")

trigram.write("===========================\n")
trigram.write("Trigrams\n")
trigram.write("===========================\n")

mcf.write("===========================\n")
mcf.write("Most Common Words \n")
mcf.write("===========================\n")

cfc.write("===========================\n")
cfc.write("Character Frequency Counts\n")
cfc.write("===========================\n")

# Reads files and finds nGrams and word counts
for i in dict_gut:
    text = read_corpus(corpus, i)
    text = text.lower()
    words = words + text
    chars = i, len(text)

    # Writes to output
    output.write(str(chars))
    output.write('\n')

    # Writes to common_word
    mcf.write(i + "\n")
    mcf.write(str(Counter(text).most_common(10)) + "\n")

    # Calculate unigrams
    unigram.write(i)
    unigram.write(str(calc_unigram(text)))
    unigram.write("\n")

    # # Calculate bigrams
    unigram.write(i)
    unigram.write(str(calc_bigram(text)))
    bigram.write("\n")

    # Calculate trigrams
    trigram.write(i)
    trigram.write(str(calc_trigram(text)))
    trigram.write("\n")

# write to char_freq
cfc.write(str(char_freq_count(words)))


# Close files
output.close()
cfc.close()
mcf.close()
unigram.close()
bigram.close()
trigram.close()
