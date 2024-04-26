import streamlit as st
from project_utils.utils import get_movie_data, truncate_title, movie_genres_sparse, get_recommendations

genres = movie_genres_sparse.columns.tolist()
options = st.multiselect(
    'Select your favorite genre combination:',
    genres,
    ['Drama', 'Romance'])


movie_combo = {genre: 0 for genre in genres}


for selection in options:
    movie_combo[selection] = 1


recommendations = get_recommendations(movie_combo)

names, posters = get_movie_data(recommendations)


if not options:
    st.write("Please select at least one genre to get recommendations.")
    st.stop()

elif options == ['Romance']:
    st.write("😏")

col1, col2 = st.columns(2)

for i in range(5):
    with col1:
        st.subheader(truncate_title(names[2*i]))
        st.image(posters[2*i])
        
    with col2:
        st.subheader(truncate_title(names[2*i+1]))
        st.image(posters[2*i+1])