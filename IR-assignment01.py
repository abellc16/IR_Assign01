from __future__ import division
import os
import re
import math
import string
from collections import Counter

#Builds the dictionsary
def make_dictionary(corpus):
    dictionary = os.listdir(corpus)
    for i in dictionary:
        print(i)
    print('\n')
    return dictionary

#Reads the corpus and prints character counts to a file.
def read_corpus(dict,corpus):
    file.write("Characters in each file: \n")
    for i in dict:
        text = open(os.path.join(corpus, i)).read()
        print(len(text))
        chars = i, len(text)
        file.write(str(chars))
        file.write('\n')


#Main function calls
corpus = "gutenberg-corpus"
file = open("output.txt", 'w')
dictionary = make_dictionary(corpus)
read_corpus(dictionary, corpus)
