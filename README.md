# Real-Time News Sentiment NLP Project

This is a complete end-to-end NLP project with:

- **Real-time dataset**: live news articles from the public NewsAPI service  
- **NLP model**: Hugging Face `transformers` sentiment analysis pipeline  
- **Web app**: Flask dashboard to search topics and view sentiment for each article  
- **Ready for deployment**: includes `requirements.txt` and `Procfile` for platforms like Render / Railway / Heroku-like PaaS.

## 1. Features

- Search any topic (e.g., "AI", "stock market", "India elections")
- Fetch latest news headlines and descriptions in real-time
- Run sentiment analysis (Positive / Negative / Neutral) on each article
- Simple, responsive web UI

## 2. Setup

### Step 1: Create virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure NewsAPI key

1. Go to `https://newsapi.org` and create a free account.
2. Get your API key.
3. Either:
   - Export it as an environment variable:

     ```bash
     export NEWS_API_KEY="YOUR_KEY_HERE"
     ```

   - Or edit `news_client.py` and replace `PUT_YOUR_NEWSAPI_KEY_HERE` with your key.

### Step 4: Run locally

```bash
python app.py
```

Open your browser at `http://127.0.0.1:5000`.

## 3. Deployment (example with Gunicorn)

Most PaaS platforms will:

- Install from `requirements.txt`
- Run the command in `Procfile`:

```bash
web: gunicorn app:app
```

Example for local test:

```bash
gunicorn app:app --bind 0.0.0.0:8000
```

Then open `http://127.0.0.1:8000`.

## 4. Project Structure

```text
.
├── app.py              # Flask web app (routes + API)
├── news_client.py      # Fetches real-time news from NewsAPI
├── nlp_model.py        # Wraps Hugging Face sentiment pipeline
├── requirements.txt
├── Procfile
├── templates
│   └── index.html      # Frontend HTML
└── static
    ├── style.css       # Styles
    └── app.js          # Frontend logic (fetch + render)
```

You can directly use this as your **NLP project** with:

- Real-time dataset
- End-to-end web interface
- Deployed using any common Python hosting platform.