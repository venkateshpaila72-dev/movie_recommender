import requests
import pickle
import pandas as pd

ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YjgyMjNkN2JkOWFhNGU1OWJhYWEzOWVkYjU3YmNjOCIsIm5iZiI6MTc4MDc1MzE4Mi4zOTM5OTk4LCJzdWIiOiI2YTI0MjMxZWVhZjJhZjMyM2RiMTYyOGMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.6VrUHS9_UjmLCMe6xm2hTfxiUz3TzrHTGq4Qw5RlkUs"  # paste your long token here

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# =====================
# TEST 1 - Access Token Test
# =====================
print("=" * 40)
print("TEST 1: Checking Access Token...")
print("=" * 40)

try:
    response = requests.get(
        "https://api.themoviedb.org/3/movie/550",
        headers=headers,
        timeout=10
    )
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        print("✅ Access Token is WORKING!")
        print("Movie Title:", response.json()['title'])
    elif response.status_code == 401:
        print("❌ Access Token is INVALID!")
    else:
        print("❌ Something went wrong:", response.json())
except Exception as e:
    print("❌ Connection Error:", e)


# ========================
# TEST 2 - Pickle File Test
# ========================
print()
print("=" * 40)
print("TEST 2: Checking Pickle Files...")
print("=" * 40)

try:
    movies_dict = pickle.load(open('movies_dictt.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    print("✅ movies_dictt.pkl loaded!")
    print("Columns:", movies.columns.tolist())
    print("Shape:", movies.shape)
except Exception as e:
    print("❌ Error loading pickle:", e)


# ========================
# TEST 3 - Poster Fetch Test
# ========================
print()
print("=" * 40)
print("TEST 3: Fetching a sample poster...")
print("=" * 40)

try:
    sample_id = movies['movie_id'].iloc[0]
    print("Using movie_id:", sample_id)
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{sample_id}",
        headers=headers,
        timeout=10
    )
    if response.status_code == 200:
        data = response.json()
        print("✅ Poster URL:", "https://image.tmdb.org/t/p/w500" + data['poster_path'])
    else:
        print("❌ Failed:", response.status_code, response.json())
except Exception as e:
    print("❌ Error:", e)