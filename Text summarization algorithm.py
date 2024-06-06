import string

def remove_punctuation(text):
    """
    Remove punctuation from the text.
    """
    return text.translate(str.maketrans('', '', string.punctuation))

def calculate_word_frequencies(text):
    """
    Calculate the frequency of each word in the text.
    """
    word_freq = {}
    words = text.split()
    for word in words:
        word = word.lower()
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1
    return word_freq

def get_top_sentences(text, word_freq, num_sentences):
    """
    Select the top N sentences based on word frequency.
    """
    sentences = text.split('.')
    sentence_scores = {}
    for sentence in sentences:
        words = sentence.split()
        score = sum(word_freq.get(word.lower(), 0) for word in words)
        sentence_scores[sentence] = score

    # Sort sentences by score and select the top N sentences
    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    top_sentences = [sentence for sentence, score in sorted_sentences[:num_sentences]]
    return top_sentences

def summarize(text, num_sentences):
    """
    Generate a summary of the text.
    """
    text = remove_punctuation(text)
    word_freq = calculate_word_frequencies(text)
    top_sentences = get_top_sentences(text, word_freq, num_sentences)
    return '. '.join(top_sentences)

# Example usage
text = """
Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural-language generation.
"""

summary = summarize(text, num_sentences=2)
print("Summary:")
print(summary)
