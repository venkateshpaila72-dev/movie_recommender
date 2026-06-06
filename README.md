# movie_prediction

# 🎬 Movie Recommender System

A content-based movie recommender system built with Python and Streamlit, powered by the TMDB 5000 Movie Dataset.

---

## 📌 Overview

This app recommends 5 similar movies based on your selection using content-based filtering. It fetches movie posters in real time from the TMDB API.

---

## 🚀 Live Demo

👉 [View on Streamlit Cloud](https://your-app-link.streamlit.app)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web app UI |
| Pandas | Data processing |
| Scikit-learn | Cosine similarity |
| TMDB API | Fetch movie posters |
| Pickle | Save ML model files |

---

## 📂 Project Structure

```
movie_recommender/
│
├── app.py                  # Main Streamlit app
├── movie_recommend_system_project.ipynb  # Jupyter notebook (model building)
├── movies_dictt.pkl        # Processed movies data
├── similarity.pkl          # Cosine similarity matrix
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ How It Works

1. **Data** — Uses TMDB 5000 Movie Dataset (two CSV files):
   - `tmdb_5000_movies.csv` — movie details (genres, keywords, overview)
   - `tmdb_5000_credits.csv` — cast and crew info

2. **Feature Engineering** — Combines genres, keywords, cast, crew, and overview into a single `tags` column

3. **Vectorization** — Converts tags to vectors using `CountVectorizer`

4. **Similarity** — Computes cosine similarity between all movies

5. **Recommendation** — Returns top 5 most similar movies with posters fetched from TMDB API

---

## 🔧 Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/movie-recommender.git
cd movie-recommender
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your TMDB Access Token
In `app.py`, replace:
```python
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"
```
Get your token at 👉 [themoviedb.org](https://www.themoviedb.org/settings/api)

### 5. Run the app
```bash
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit
pandas
requests
scikit-learn
numpy
```

---

## 🌐 Deploy on Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set `ACCESS_TOKEN` in **Secrets**:
```toml
ACCESS_TOKEN = "your_token_here"
```
5. Click **Deploy!**

---

## 📊 Dataset

- **Source:** [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Size:** ~5000 movies
- **Files:** `tmdb_5000_movies.csv` + `tmdb_5000_credits.csv`

---

## 🙌 Acknowledgements

- [The Movie Database (TMDB)](https://www.themoviedb.org) for the API and dataset
- [Streamlit](https://streamlit.io) for the awesome framework

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).