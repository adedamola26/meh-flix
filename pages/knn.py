import streamlit as st
from project_utils.utils import get_movie_data, truncate_title, movie_df, get_neighbours


st.set_page_config(
    page_title="Find Songs Similar to Yours🎤", page_icon="🎤", layout="wide"
)


    
movie_choice = st.selectbox(
    'Your favorite movie:',
    movie_df.title,
    1261
) 


if st.button('Recommend'):
    recommendations = get_neighbours(movie_choice)
    names, posters = get_movie_data(recommendations)

    col1, col2 = st.columns(2)
    for i in range(5):
        with col1:
            st.subheader(truncate_title(names[2*i]))
            st.image(posters[2*i])
            
        with col2:
            st.subheader(truncate_title(names[2*i+1]))
            st.image(posters[2*i+1])
            