from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.model = pipeline("sentiment-analysis")

    def analyze(self, text):
        return self.model(text)[0]
