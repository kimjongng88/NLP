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
from sklearn.preprocessing import normalize


vocab = open("brown_vocab_100.txt")

#load the indices dictionary
word_index_dict = {}
for i, line in enumerate(vocab):
    word_index_dict[line.rstrip()] = i

f = open("brown_100.txt")

counts = np.zeros((len(word_index_dict), len(word_index_dict)))
counts += 0.1

for line in f:
    words = line.split()

    previous_word = '<s>'

    for word in words[1:]:
        counts[word_index_dict[previous_word.lower()], word_index_dict[word.lower()]] += 1

        previous_word = word

f.close()

probs = normalize(counts, norm='l1', axis=1)

with open("smooth_probs.txt", "w") as f:
    f.write(f"{probs[word_index_dict['all'], word_index_dict['the']]}\n")
    f.write(f"{probs[word_index_dict['the'], word_index_dict['jury']]}\n")
    f.write(f"{probs[word_index_dict['the'], word_index_dict['campaign']]}\n")
    f.write(f"{probs[word_index_dict['anonymous'], word_index_dict['calls']]}\n")
