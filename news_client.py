import os
import requests
from typing import List, Dict

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "PUT_YOUR_NEWSAPI_KEY_HERE")
NEWS_API_URL = "https://newsapi.org/v2/everything"

def fetch_latest_news(query: str, page_size: int = 10) -> List[Dict]:
    """Fetch latest news articles for a query using NewsAPI.
    You must create a free account on https://newsapi.org and put your API key in
    an environment variable NEWS_API_KEY or replace the constant above.
    """
    params = {
        "q": query,
        "pageSize": page_size,
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
    }
    try:
        resp = requests.get(NEWS_API_URL, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        articles = data.get("articles", [])
        normalized = []
        for a in articles:
            normalized.append(
                {
                    "title": a.get("title"),
                    "description": a.get("description"),
                    "url": a.get("url"),
                    "source": (a.get("source") or {}).get("name"),
                    "publishedAt": a.get("publishedAt"),
                }
            )
        return normalized
    except Exception as e:
        print("Error fetching news:", e)
        return []