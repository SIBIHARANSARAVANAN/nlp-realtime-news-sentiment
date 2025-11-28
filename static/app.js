const resultsEl = document.getElementById("results");
const formEl = document.getElementById("search-form");
const queryInputEl = document.getElementById("query-input");
const autoRefreshToggle = document.getElementById("auto-refresh-toggle");

let currentQuery = queryInputEl.value || "artificial intelligence";
let refreshTimer = null;

async function fetchArticles(query) {
    try {
        resultsEl.innerHTML = "<p>Loading...</p>";
        const res = await fetch(`/api/articles?query=${encodeURIComponent(query)}`);
        const data = await res.json();
        renderArticles(data.articles || []);
    } catch (err) {
        console.error(err);
        resultsEl.innerHTML = "<p>Failed to load articles. Check console for details.</p>";
    }
}

function renderArticles(articles) {
    if (!articles.length) {
        resultsEl.innerHTML = "<p>No articles found for this topic.</p>";
        return;
    }

    resultsEl.innerHTML = "";
    articles.forEach((article) => {
        const card = document.createElement("article");
        card.className = "article-card";

        const header = document.createElement("div");
        header.className = "article-header";

        const title = document.createElement("a");
        title.className = "article-title";
        title.href = article.url || "#";
        title.target = "_blank";
        title.rel = "noopener noreferrer";
        title.textContent = article.title || "Untitled";

        const sentiment = document.createElement("span");
        const label = article.sentiment?.label || "NEUTRAL";
        const score = article.sentiment?.score ?? 0;
        sentiment.className = `sentiment-badge sentiment-${label}`;
        sentiment.textContent = `${label} (${(score * 100).toFixed(1)}%)`;

        header.appendChild(title);
        header.appendChild(sentiment);

        const meta = document.createElement("div");
        meta.className = "article-meta";
        const source = article.source || "Unknown source";
        const published = article.publishedAt
            ? new Date(article.publishedAt).toLocaleString()
            : "Unknown time";
        meta.textContent = `${source} · ${published}`;

        const desc = document.createElement("p");
        desc.className = "article-description";
        desc.textContent = article.description || "No description available.";

        card.appendChild(header);
        card.appendChild(meta);
        card.appendChild(desc);

        resultsEl.appendChild(card);
    });
}

formEl.addEventListener("submit", (e) => {
    e.preventDefault();
    const q = queryInputEl.value.trim();
    if (!q) return;
    currentQuery = q;
    fetchArticles(currentQuery);
});

autoRefreshToggle.addEventListener("change", () => {
    setupAutoRefresh();
});

function setupAutoRefresh() {
    if (refreshTimer) {
        clearInterval(refreshTimer);
        refreshTimer = null;
    }
    if (autoRefreshToggle.checked) {
        refreshTimer = setInterval(() => {
            fetchArticles(currentQuery);
        }, 60000); // 60s
    }
}

// Initial load
fetchArticles(currentQuery);
setupAutoRefresh();