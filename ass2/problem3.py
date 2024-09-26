#!/usr/bin/env python3

"""
NLP A2: N-Gram Language Models

@author: Klinton Bicknell, Harry Eldridge, Nathan Schneider, Lucia Donatelli, Alexander Koller

DO NOT SHARE/DISTRIBUTE SOLUTIONS WITHOUT THE INSTRUCTOR'S PERMISSION
"""

import numpy as np
from sklearn.preprocessing import normalize
from generate import GENERATE
import random
import codecs


vocab = codecs.open("brown_vocab_100.txt")

'''
#load the indices dictionary
word_index_dict = {}
for i, line in enumerate(vocab):
    #TODO: import part 1 code to build dictionary
'''
 # Load the indices dictionary
word_index_dict = {}
for i, line in enumerate(vocab):
    word = line.strip()
    word_index_dict[word] = i

vocab.close()

# Load the corpus
f = codecs.open("brown_100.txt")


counts = np.zeros((len(word_index_dict), len(word_index_dict)))#TODO: initialize numpy 0s array


#TODO: iterate through file and update counts
for sentence in f:
    words = sentence.strip().lower().split()
    words.append('</s>')
    for i in range(len(words) - 1):
        word1 = word_index_dict.get(words[i], -1)
        word2 = word_index_dict.get(words[i + 1], -1)
        if word1 != -1 and word2 != -1:
            counts[word1][word2] += 1

f.close()

#TODO: normalize counts
row_sums = counts.sum(axis=1, keepdims=True)
mle_probs = counts / row_sums

#TODO: writeout bigram probabilities
with open('bigram_probs.txt', 'w') as file:
    for word1, row in enumerate(mle_probs):
        for word2, prob in enumerate(row):
            if prob > 0:
                word1_word = list(word_index_dict.keys())[word1]
                word2_word = list(word_index_dict.keys())[word2]
                file.write(f"{word1_word}\t{word2_word}\t{prob}\n")


f.close()
