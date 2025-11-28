from flask import Flask, render_template, request, jsonify
from news_client import fetch_latest_news
from nlp_model import SentimentAnalyzer

app = Flask(__name__)
sentiment_analyzer = SentimentAnalyzer()

@app.route("/")
def index():
    query = request.args.get("query", "artificial intelligence")
    return render_template("index.html", default_query=query)

@app.route("/api/articles")
def api_articles():
    query = request.args.get("query", "artificial intelligence")
    articles = fetch_latest_news(query=query, page_size=10)

    # Add sentiment to each article
    for article in articles:
        text = article.get("title", "") + ". " + article.get("description", "")
        if text.strip():
            sentiment = sentiment_analyzer.predict(text)
        else:
            sentiment = {"label": "NEUTRAL", "score": 0.0}
        article["sentiment"] = sentiment
    return jsonify({"query": query, "articles": articles})

if __name__ == "__main__":
    # For local development
    app.run(host="0.0.0.0", port=5000, debug=True)