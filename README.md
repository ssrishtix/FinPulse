# 💹 FinPulse

> **Tracking the emotional pulse of markets to make smarter investment decisions.**

FinPulse is an AI-powered stock advisory system that blends **behavioral finance**, **real-time market data**, and **sentiment analysis** to help users avoid emotional and bias-driven investment mistakes.

---

## 🚀 Features

- 📈 Real-time stock data ingestion and analysis
- 📰 Financial news sentiment analysis (via NLP)
- 🧠 Behavioral bias detection (e.g., herd mentality, overconfidence)
- 💬 Personalized decision-making insights
- 🛠️ REST API powered by FastAPI

---

## 🧱 Tech Stack

| Layer              | Technologies                                |
|--------------------|---------------------------------------------|
| Backend API        | FastAPI, Python                             |
| Data Ingestion     | yfinance, News APIs, `requests`             |
| Database           | PostgreSQL + SQLAlchemy ORM                 |
| ML & NLP Models    | Scikit-learn, HuggingFace Transformers      |
| Deployment (later) | Render / GitHub Actions                     |

---

## 📊 Modules (MVP Scope)

- `StockModule`: Historical + live stock data
- `SentimentModule`: Analyzes news headlines for market sentiment
- `BiasDetector`: Detects common behavioral biases using ML logic
- `AdvisoryEngine`: Generates actionable advice based on detected biases

---

## 📌 Getting Started

```bash
# Clone the repo
git clone https://github.com/yourusername/FinPulse.git
cd FinPulse

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run FastAPI app
uvicorn main:app --reload
