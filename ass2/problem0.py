import nltk
import matplotlib.pyplot as plt

# Load the Brown corpus
#nltk.download('brown')
from nltk.corpus import brown

#Our chosen genres, which are news and science fiction
genres = ['news','science_fiction']

# Function to compute word frequencies
def get_frequencies(genre):
    words = brown.words(categories=genre)
    a = nltk.FreqDist(words)
    return a

# Get frequency per word
freq_whole = get_frequencies(None)
ranks_whole = list(range(1, len(freq_whole) + 1))

# Word freq for news and science fiction
word_freq_by_genre = {}
for i in genres:
    word_freq = get_frequencies(i)
    word_freq_by_genre[i] = word_freq

# Extract additional information
tokens_whole = len(brown.words()) # Number of tokens
ntypes_whole = len(freq_whole) # Types
nwords_whole = len(set(w.lower() for w in brown.words())) # Number of words
avgws_corp = nwords_whole / len(brown.sents()) # Average words per scentence
avgwl_corpus = sum(len(word) for word in brown.words()) / nwords_whole # Average word length

# Speech tags
speech = nltk.FreqDist(tag for (word, tag) in brown.tagged_words())
#t10_pos = speech.most_common(10)
# Compute frequency distribution of POS tags
freq_dist = nltk.FreqDist(speech)
'''
# Plot frequency curves for the whole corpus and two genres
plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(ranks_whole,freq_whole.values(), label='Whole Corpus')
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.title('Frequency Curve for Whole Corpus')
plt.legend()
plt.subplot(2, 1, 2)
for genre in genres:
    plt.plot(range(1, len(word_freq_by_genre[genre]) + 1),word_freq_by_genre[genre].values(), label=genre)
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.title('Frequency Curves for Genres')
plt.legend()
plt.tight_layout()

# Plot frequency curves with log-log axes for the whole corpus and two genres
plt.figure(figsize=(6, 6))
plt.subplot(2, 1, 1)
plt.loglog(ranks_whole, freq_whole.values(), label='Whole Corpus')
plt.xlabel('Word Rank (log scale)')
plt.ylabel('Frequency (log scale)')
plt.title('Frequency Curve with Log-Log Axes for Whole Corpus')
plt.legend()
plt.subplot(2, 1, 2)
for genre in genres:
    plt.loglog(list(range(1, len(word_freq_by_genre[genre]) + 1)),list(word_freq_by_genre[genre].values()), label=genre)
plt.xlabel('Word Rank (log scale)')
plt.ylabel('Frequency (log scale)')
plt.title('Frequency Curves with Log-Log Axes for Genres')
plt.legend()
plt.tight_layout()

plt.show()
'''
# Important information
print("# tokens in the whole corpus:", tokens_whole)
print("# types in the whole corpus:", ntypes_whole)
print("# words in the whole corpus:", nwords_whole)
print("Average number of words per sentence in the whole corpus:", avgws_corp)
print("Average word length in the whole corpus:", avgwl_corpus)
#print("Top 10 part-of-speech:", t10_pos)
print("Top 10 most frequent POS tags in the Brown Corpus:")
for pos, freq in freq_dist.most_common(10):
    print(f"{pos}: {freq}")

