from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        # Loads a small but strong sentiment model
        self.pipe = pipeline("sentiment-analysis")

    def predict(self, text: str):
        try:
            res = self.pipe(text[:512])[0]  # limit length for speed
            # Normalize label
            label = res["label"].upper()
            if label in ["POSITIVE", "NEGATIVE"]:
                norm_label = label
            else:
                # Some models use LABEL_0 / LABEL_1 etc.
                norm_label = label
            return {"label": norm_label, "score": float(res["score"])}
        except Exception as e:
            # Fallback as neutral
            return {"label": "NEUTRAL", "score": 0.0}