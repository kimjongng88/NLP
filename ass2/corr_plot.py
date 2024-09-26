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

# Word freq for news and science fiction
word_freq_by_genre = {}
for i in genres:
    word_freq = get_frequencies(i)
    word_freq_by_genre[i] = word_freq

# Extract additional information
tokens_whole = len(brown.sents()) # Number of tokens
ntypes_whole = len(freq_whole) # Types
nwords_whole = len(brown.words()) # Number of words
avgws_corp = nwords_whole / len(brown.sents()) # Average words per scentence
avgwl_corpus = sum(len(word) for word in brown.words()) / nwords_whole # Average word length

# Speech tags
speech = nltk.FreqDist(tag for (word, tag) in brown.tagged_words())
#t10_pos = speech.most_common(10)
# Compute frequency distribution of POS tags
freq_dist = nltk.FreqDist(speech)

sorted_words = sorted(freq_whole.items(), key=lambda x: x[1], reverse=True)
# Get ranks and frequencies
ranks = list(range(1, len(sorted_words) + 1))
frequencies = [freq for word, freq in sorted_words]

print(len(ranks),"length")


# Plot frequency curves for the whole corpus and two genres
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(ranks, frequencies, label='Whole Corpus')
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.title('Word Frequency vs. Rank in Brown Corpus')
plt.legend()
plt.subplot(2, 1, 2)
for genre in genres:
    sorted_words_g1 = sorted(word_freq_by_genre[genre].items(), key=lambda x: x[1], reverse=True)
    # Get ranks and frequencies
    ranks_g1 = list(range(1, len(sorted_words_g1) + 1))
    frequencies_g1 = [freq for word, freq in sorted_words_g1]
    plt.plot(ranks_g1,frequencies_g1, label=genre)
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.title('Frequency Curves for Genres')
plt.legend()
plt.tight_layout()

# Plot frequency curves with log-log axes for the whole corpus and news + sci
plt.figure(figsize=(6, 6))
plt.subplot(2, 1, 1)
plt.loglog(ranks, frequencies, label='Whole Corpus')
plt.xlabel('Word Rank (log scale)')
plt.ylabel('Frequency (log scale)')
plt.title('Frequency Curve with Log-Log Axes for Whole Corpus')
plt.legend()
plt.subplot(2, 1, 2)
for genre in genres:
    sorted_words_g = sorted(word_freq_by_genre[genre].items(), key=lambda x: x[1], reverse=True)
    ranks = list(range(1, len(sorted_words_g) + 1))
    frequencies = [freq for word, freq in sorted_words_g]
    plt.loglog(ranks,frequencies, label=genre)
plt.xlabel('Word Rank (log scale)')
plt.ylabel('Frequency (log scale)')
plt.title('Frequency Curves with Log-Log Axes for Genres')
plt.legend()
plt.tight_layout()

plt.show()

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
