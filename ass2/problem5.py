import numpy as np
from sklearn.preprocessing import normalize

vocab = open("brown_vocab_100.txt")

# load the indices dictionary
word_index_dict = {}
for i, line in enumerate(vocab):
    word_index_dict[line.rstrip()] = i

f = open("brown_100.txt")

counts = np.zeros((len(word_index_dict), len(word_index_dict), len(word_index_dict)))
#counts += 0.1 # For smoothing

for line in f:
    words = line.split()

    prev_prev_word = '<s>'
    prev_word = '<s>'

    for word in words[1:]:
        counts[word_index_dict[prev_prev_word.lower()], word_index_dict[prev_word.lower()], word_index_dict[word.lower()]] += 1

        prev_prev_word = prev_word
        prev_word = word

f.close()

# normalize probabilities along the third axis
probs = counts / np.sum(counts, axis=2, keepdims=True)

with open("unsmooth_probs_5.txt", "w") as f:# Change file name for smoothing
    f.write(f"{probs[word_index_dict['in'], word_index_dict['the'], word_index_dict['past']]}\n")
    f.write(f"{probs[word_index_dict['in'], word_index_dict['the'], word_index_dict['time']]}\n")
    f.write(f"{probs[word_index_dict['the'], word_index_dict['jury'], word_index_dict['said']]}\n")
    f.write(f"{probs[word_index_dict['the'], word_index_dict['jury'], word_index_dict['recommended']]}\n")
    f.write(f"{probs[word_index_dict['jury'], word_index_dict['said'], word_index_dict['that']]}\n")
    f.write(f"{probs[word_index_dict['agriculture'], word_index_dict['teacher'], word_index_dict[',']]}\n")
