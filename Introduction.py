import streamlit as st

st.set_page_config(
    page_title="Meh-flix", page_icon="🙃", layout = "centered"
)

st.title("~Netflix~ Meh-flix 🙃")

st.markdown("This is a movie recommender system that... you guessed it.... recommends movies to you....based on your choices.")

st.markdown("You can get recommendations in two ways:")
st.markdown("- Content-based")
st.markdown("- Collaborative filtering (item-based)")

st.markdown("For the **content-based**, you can select up to 5 different genres and the app suggests the top ten movies that best match your genre combo.")

st.markdown("_Not sure about the genre combo you prefer but know the name of a movie you really like?_")

st.markdown("The **collaborative filtering** recommender system has got you covered!")

st.markdown("You type in the name of the movie you really like and...if it's among our 3,675 movies...you'll find it.")

st.markdown("Once you find it... select it, click the 'Recommend' button and you'll get the top 10 most \"similar\" movies.")

st.markdown("By \"similar\" we mean... movies that have similar raters and similar ratings from those raters.")

st.markdown("In other words... people who enjoy the movie you've selected tend to also enjoy the movies we recommend.")

st.markdown("**PS**:")

st.markdown("- The available movies were produced between 1919 and 2000. 👴")

st.markdown("- The technical details are covered in this [Jupyter Notebook](). 🤓")

st.markdown("Enjoy your recommendations! 🍿🎬")
