import streamlit as st

st.set_page_config(
    page_title="Meh-flix", page_icon="🙃", layout = "centered"
)

st.title("~Netflix~ Meh-flix 🙃")

st.markdown("""
This is a movie recommender system that... you guessed it.... recommends movies to you....based on your choices.

You can get recommendations in two ways:
- Content-based
- Collaborative filtering (item-based)

For the **content-based**, you can select up to 5 different genres and the app suggests the top ten movies that best match your genre combo.

_Not sure about the genre combo you prefer but know the name of a movie you really like?_

The **collaborative filtering** recommender system has got you covered!

You can type in the name of the movie you really like and...if it's among our 3,675 movies...you'll find it.

Once you find it... select it, click the 'Recommend' button and you'll get the top 10 most "similar" movies.

By "similar" we mean... movies that have similar raters and similar ratings from those raters.

In other words... people who enjoy the movie you've selected tend to also enjoy the movies we recommend.

**PS**:
- The available movies were produced between 1919 and 2000. 👴
- [Click me for technical details](https://github.com/adedamola26/meh-flix2.0?tab=readme-ov-file#nefflix-meh-flix----movie-recommender-system-project). 🤓
            
You can click on the sidebar to get started! 🚀

Enjoy your recommendations! 🍿🎬
""")
