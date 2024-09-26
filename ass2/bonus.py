import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist
from math import log2

corpus = brown.words()
corpus = [word.lower() for word in corpus if word.isalpha()]
fd = FreqDist(corpus)
vocabulary = [word for word in fd if fd[word] >= 10]
corpus = [word for word in corpus if word in vocabulary]

# Calculate PMI values 
word_pairs = []
for i in range(len(corpus)-1):
    word1 = corpus[i]
    word2 = corpus[i+1]
    word_pairs.append((word1, word2))
fd_pairs = FreqDist(word_pairs)
pmi_pairs = {}
for pair in fd_pairs:
    w1, w2 = pair
    p_w1 = fd[w1] / len(corpus)
    p_w2 = fd[w2] / len(corpus)
    p_w1w2 = fd_pairs[pair] / len(corpus)
    pmi = log2(p_w1w2 / (p_w1 * p_w2))
    pmi_pairs[pair] = pmi

# Highest PMI values
sorted_pmi_pairs = sorted(pmi_pairs.items(), key=lambda x: x[1], reverse=True)
top = sorted_pmi_pairs[:20]

# Lowest PMI values
last = sorted_pmi_pairs[-20:]


top_table = ""
for pair, pmi in top:
    top_table += "{} & {} & {:.2f} \\\\\n".format(pair[0], pair[1], pmi)


bottom_table = ""
for pair, pmi in last:
    bottom_table += "{} & {} & {:.2f} \\\\\n".format(pair[0], pair[1], pmi)

# LaTeX
print("Top 20 word pairs with highest PMI values:")
print("\\begin{tabular}{llr}")
print("Word 1 & Word 2 & PMI \\\\")
print("\\hline")
print(top_table)
print("\\end{tabular}\n\n")

print("Bottom 20 word pairs with lowest PMI values:")
print("\\begin{tabular}{llr}")
print("Word 1 & Word 2 & PMI \\\\")
print("\\hline")
print(bottom_table)
print("\\end{tabular}")
