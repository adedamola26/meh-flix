import streamlit as st

st.title("~Netflix~ Meh-Flix 🙃")

st.markdown("This is movie recommender system that... you guessed it.... recommends movies to you....based on your choices.")

st.markdown("You can get recommendations in two ways:")
st.markdown("- content-based")
st.markdown("- collaborative filtering (item-based)")

st.markdown("For the content-based, you can select up to 5 different genres and the recommender system suggests the top ten movies that best match your selection.")

st.markdown("Don't know the genre combination you prefer but know the name of a movie you really like?")

st.markdown("The collaborative filtering recommender system has got you covered.")

st.markdown("You type in the name of the movie you really like... and if it's among our 3,765 movies...you'll see it.")

st.markdown("Once you see it...")

st.markdown("Select it and click the 'Recommend' button and you'll get the top 10 most \"similar\" movies.")

st.markdown("\"similar\" as in... what other people who like you movie selection... also tend to like.")

st.markdown("Note: the movies listed were produced between 1919 and 2000. 👴")

st.markdown("Enjoy your recommendations! 🍿🎬")
