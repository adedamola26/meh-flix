import streamlit as st
from project_utils.utils import get_movie_data, movie_df, get_neighbours, get_and_resize_image


st.set_page_config(
    page_title="Collaborative-filtering", page_icon="👥", layout="wide"
)

st.title("Collaborative Filtering Recommender System")

st.text("What other movies do people tend to enjoy alongside your choice?")

movie_choice = st.selectbox(
    'Select your favorite movie:',
    movie_df.title,
    1
) 


if st.button('Recommend'):
    st.header(f"People who like {movie_choice} also like:")
    recommendations = get_neighbours(movie_choice)
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
            