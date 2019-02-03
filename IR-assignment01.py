import os
from collections import Counter


# Builds the dictionary
# from typing import Dict, Any
def make_dictionary(corpus):
    dict_gut = os.listdir(corpus)
    for i in dict_gut:
        print(i)
    print('\n')
    return dict_gut


# Reads the corpus file by file
def read_corpus(dict_gut, corpus):
    file.write("Characters in each file: \n")
    for i in dict_gut:
        text = open(os.path.join(corpus, i)).read()
        print(len(text))
        chars = i, len(text)
        file.write(str(chars))
        file.write('\n')

        # Writes to common_word
        mcf.write(i + "\n")
        mcf.write(str(Counter(text).most_common(10)) + "\n")

        # Calculate unigrams
        # unigram.write(i)
        # unigram.write(str(calc_unigram(text)))
        # unigram.write("\n")
        #
        # # Calculate bigrams
        # unigram.write(i)
        # unigram.write(str(calc_bigram(text)))
        # bigram.write("\n")
        #
        # # Calculate trigrams
        # trigram.write(i)
        # trigram.write(str(calc_trigram(text)))
        # trigram.write("\n")
        

# Frequency count of all characters in a text.
def char_freq_count(text):
    return Counter(ch for ch in text.lower() if ch.isalpha())


# Creates one string for all of the files.
def all_words(dict_gut):
    wrds = ""
    for doc in dict_gut:
        text = open(os.path.join(corpus, doc)).read()
        wrds = wrds + text

    return wrds


# Find all unigrams in a document
def calc_unigram(text):
    text = text.split(' ')
    uni = []
    for w in range(len(text)):
        uni.append(text[w])

    return sorted(uni)


# Find all bigrams in a document
def calc_bigram(text):
    text = text.split(' ')
    bi = []
    for w in range(len(text) - 1):
        bi.append((text[w], text[w + 1]))

    return sorted(bi)


# Find all trigrams of each document
def calc_trigram(text):
    text = text.split(' ')
    tri = []
    for w in range(len(text) - 2):
        tri.append((text[w], text[w + 1], text[w + 2]))

    return sorted(tri)

# Counts the frequency of n-grams and returns them in
# descending order
def ngram_counter(text):
    counter = Counter(text)
    return counter.most_common()


# Main function calls
corpus = "gutenberg-corpus"
file = open("output.txt", 'w')
cfc = open("char_freq.txt", 'w')
mcf = open('common_word.txt', 'w')
unigram = open('unigram.txt', 'w')
bigram = open('bigram.txt', 'w')
trigram = open('trigram.txt', 'w')

dict_gut = make_dictionary(corpus)
mcf.write("===========================\n")
mcf.write("Most Common Words \n")
mcf.write("===========================\n")
read_corpus(dict_gut, corpus)

new_str = all_words(dict_gut)
cfc.write("===========================\n")
cfc.write("Character Frequency Counts\n")
cfc.write("===========================\n")
cfc.write(str(char_freq_count(new_str)))

test = "hello how what are you doing at 8?"
u_test = calc_unigram(test)
b_test = calc_bigram(test)
t_test = calc_trigram(test)

# Formatting for readability of unigrams.txt
unigram.write("===========================\n")
unigram.write("Unigrams\n")
unigram.write("===========================\n")
unigram.write(str(u_test)) # Write unigrams to .txt
unigram.write("\n===========================\n")
unigram.write("Unigram Frequencies\n")
unigram.write("===========================\n")
unigram.write(str(ngram_counter(u_test)))

# Formatting for readability of bigrams.txt
bigram.write("===========================\n")
bigram.write("Bigrams\n")
bigram.write("===========================\n")
bigram.write(str(b_test)) # Write bigrams to .txt
bigram.write("\n===========================\n")
bigram.write("Bigram frequencies\n")
bigram.write("===========================\n")
bigram.write(str(ngram_counter(b_test)))

# Formatting for readability of trigrams.txt
trigram.write("===========================\n")
trigram.write("Trigrams\n")
trigram.write("===========================\n")
trigram.write(str(t_test)) # Write trigrams to .txt
trigram.write("\n===========================\n")
trigram.write("Trigram frequencies\n")
trigram.write("===========================\n")
trigram.write(str(ngram_counter(t_test)))

file.close()
cfc.close()
mcf.close()
unigram.close()
bigram.close()
trigram.close()