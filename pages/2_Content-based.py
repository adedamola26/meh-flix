import streamlit as st
from project_utils.utils import get_movie_data, truncate_title, movie_genres_sparse, get_recommendations, get_and_resize_image

st.set_page_config(
    page_title="Content-based", page_icon="🧺", layout = "wide"
)

genres = movie_genres_sparse.columns.tolist()
options = st.multiselect(
    'You can select up to 5 different genres:',
    genres,
    ['Drama', 'Romance'],
    max_selections = 5)


movie_combo = {genre: 0 for genre in genres}


for selection in options:
    movie_combo[selection] = 1


if not options:
    st.write("Please select at least one genre to get recommendations.")
    st.stop()

elif options == ['Romance']:
    st.write("😏")


recommendations = get_recommendations(movie_combo)

names, images_url = get_movie_data(recommendations)

col1, col2 = st.columns(2)


for i in range(5):
    with col1:
        st.subheader(names[2*i])
        image = get_and_resize_image(images_url[2*i], 750)
        st.image(image)
        
    with col2:
        st.subheader(names[2*i+1])
        image = get_and_resize_image(images_url[2*i+1], 750)
        st.image(image)