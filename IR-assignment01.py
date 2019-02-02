import os
import re
import math
import string
from collections import Counter


# Builds the dictionary
from typing import Dict, Any


def make_dictionary(corpus):
    dict_gut = os.listdir(corpus)
    for i in dict_gut:
        print(i)
    print('\n')
    return dict_gut


# Reads the corpus file by file
def read_corpus(dict_gut, corpus):
    file.write("Characters in each file: \n")
    mcf.write("===========================\n")
    mcf.write("Most Common Words \n")
    mcf.write("===========================\n")
    for i in dict_gut:
        text = open(os.path.join(corpus, i)).read()
        print(len(text))
        chars = i, len(text)
        file.write(str(chars))
        file.write('\n')

        # Writes to common_word
        mcf.write(i + "\n")
        mcf.write(str(Counter(text).most_common(10)) + "\n")
        

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


# Main function calls
corpus = "gutenberg-corpus"
file = open("output.txt", 'w')
cfc = open("char_freq.txt", 'w')
mcf = open('common_word.txt', 'w')

dict_gut = make_dictionary(corpus)
read_corpus(dict_gut, corpus)

new_str = all_words(dict_gut)
cfc.write("===========================\n")
cfc.write("Character Frequency Counts\n")
cfc.write("===========================\n")
cfc.write(str(char_freq_count(new_str)))

file.close()
cfc.close()
mcf.close()