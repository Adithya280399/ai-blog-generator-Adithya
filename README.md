# AI-Powered Blog Post Generator 🧠📝

This is a Flask-based backend application that uses OpenAI's GPT model to automatically generate SEO-optimized blog posts based on a given keyword. It also supports daily automation and preview-friendly HTML output.

---

## 🚀 Features

- 🔍 Mock SEO data fetcher (`search volume`, `keyword difficulty`, `CPC`)
- ✨ Blog content generated via OpenAI (GPT-3.5 / GPT-4)
- 📂 Blog posts saved locally as `.html` with clean, readable styling
- 🔁 Optional: daily automation using scheduler or cron
- ✅ REST API: `GET /generate?keyword=your_keyword`

---

## 📁 Folder Structure
├── app.py
├── ai_generator.py
├── seo_fetcher.py
├── scheduler.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── generated_posts/

## 🧪 How to Run

### 1. Clone this repo

git clone https://github.com/<your-username>/ai-blog-generator-interview-Adithya.git
cd ai-blog-generator-interview-Adithya

### 2. Set up environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

### 3.Create a .env file
OPENAI_API_KEY=sk-...

### 4.Start the Flask server
python app.py
