import streamlit as st
import pickle
import pandas as pd
import requests
import time

ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YjgyMjNkN2JkOWFhNGU1OWJhYWEzOWVkYjU3YmNjOCIsIm5iZiI6MTc4MDc1MzE4Mi4zOTM5OTk4LCJzdWIiOiI2YTI0MjMxZWVhZjJhZjMyM2RiMTYyOGMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.6VrUHS9_UjmLCMe6xm2hTfxiUz3TzrHTGq4Qw5RlkUs"  # paste your long token here

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    for attempt in range(3):  # retry 3 times
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if 'poster_path' in data and data['poster_path']:
                    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
        except:
            time.sleep(0.5)
            continue
    return None


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        time.sleep(0.5)

    return recommended_movies, recommended_movies_posters


# Load data
movies_dict = pickle.load(open('movies_dictt.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# UI
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values)

if st.button('Recommend'):
    with st.spinner('Fetching recommendations...'):
        name, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(posters[0] if posters[0] else "https://via.placeholder.com/500")

    with col2:
        st.text(name[1])
        st.image(posters[1] if posters[1] else "https://via.placeholder.com/500")

    with col3:
        st.text(name[2])
        st.image(posters[2] if posters[2] else "https://via.placeholder.com/500")

    with col4:
        st.text(name[3])
        st.image(posters[3] if posters[3] else "https://via.placeholder.com/500")

    with col5:
        st.text(name[4])
        st.image(posters[4] if posters[4] else "https://via.placeholder.com/500")