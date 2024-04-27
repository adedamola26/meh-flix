import streamlit as st
from project_utils.utils import get_movie_data, truncate_title, movie_df, get_neighbours, get_and_resize_image


st.set_page_config(
    page_title="Collaborative-filtering", page_icon="👥", layout="wide"
)

movie_choice = st.selectbox(
    'Your favorite movie:',
    movie_df.title,
    1261
) 


if st.button('Recommend'):
    recommendations = get_neighbours(movie_choice)
    names, images_url = get_movie_data(recommendations)

    col1, col2 = st.columns(2)
    for i in range(5):
        with col1:
            st.subheader(truncate_title(names[2*i]))
            image = get_and_resize_image(images_url[2*i], 750)
            st.image(image)
            
        with col2:
            st.subheader(truncate_title(names[2*i+1]))
            image = get_and_resize_image(images_url[2*i+1], 750)
            st.image(image)
            