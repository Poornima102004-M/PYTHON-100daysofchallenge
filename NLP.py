import re

class SentimentAnalyzer:
    def __init__(self, positive_words, negative_words):
        self.positive_words = positive_words
        self.negative_words = negative_words

    def analyze_sentiment(self, text):
        # Clean the text
        text = self.clean_text(text)
        
        # Tokenize the text
        words = text.split()

        # Calculate sentiment score
        sentiment_score = sum(1 for word in words if word in self.positive_words) - \
                          sum(1 for word in words if word in self.negative_words)
        
        # Determine sentiment
        if sentiment_score > 0:
            return 'positive'
        elif sentiment_score < 0:
            return 'negative'
        else:
            return 'neutral'

    def clean_text(self, text):
        # Remove special characters and lowercase the text
        text = re.sub(r'[^A-Za-z0-9\s]', '', text.lower())
        return text

# Example usage:
positive_words = set(["good", "happy", "awesome", "great"])
negative_words = set(["bad", "sad", "awful", "terrible"])
analyzer = SentimentAnalyzer(positive_words, negative_words)
text = "I'm feeling good today, but the weather is bad."
sentiment = analyzer.analyze_sentiment(text)
print("Sentiment:", sentiment)
