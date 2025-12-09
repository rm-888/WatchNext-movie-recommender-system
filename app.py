import streamlit as st
import pickle
import pandas as pd
import requests
from huggingface_hub import hf_hub_download

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5af90b957d32b90fbd642ea93912f26e&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

model_path = hf_hub_download(
    repo_id="rm-888/watchnext-similarity", 
    filename="simi.pkl",
    repo_type="dataset"
)

with open(model_path, "rb") as f:
    similarity = pickle.load(f)
    
#similarity = pickle.load(open('simi.pkl', 'rb'))
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

def recommend(movie):
    movie_ind = movies[movies['title']==movie].index[0]
    distances = similarity[movie_ind]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetching poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster



st.title("🔎 WatchNext: Movie Recommender")
st.markdown("Still stuck on that last movie you watched??")
st.markdown("No worries... Just search your movie and we will recommend another one to watch based on your choice!")


selected_movie_name = st.selectbox(
    'Choose the movie of your choice',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            st.image(poster)

footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f1f1f1;
    text-align: center;
    padding: 10px;
    font-size: 14px;
    color: #333;
}
</style>

<div class="footer">
    © 2025 WatchNext: Movie Recommender | Built with Streamlit<br>
    With ❤️ by rm-888
</div>
"""


st.markdown(footer, unsafe_allow_html=True)


