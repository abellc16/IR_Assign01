import os
import re
import math
import string
from collections import Counter


# Builds the dictionary
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

        # Writes character frequency to a file
        cfc.write(i + "\n")
        cfc.write(str(char_freq_count(text)) + "\n\n")
        
        #Writes to common_word
        mcf.write(i + "\n")
        mcf.write(str(Counter(text).most_common(10)) + "\n")
        

# Frequency count of all characters in a text.
def char_freq_count(text):
    freq = {}
    for w in text:
        keys = freq.keys()
        if w in keys:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq

    

# Main function calls
corpus = "gutenberg-corpus"
file = open("output.txt", 'w')
cfc = open("char_freq.txt", 'w')
mcf = open('common_word.txt', 'w')

dict_gut = make_dictionary(corpus)
read_corpus(dict_gut, corpus)

