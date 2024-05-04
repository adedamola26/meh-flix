# ~Nefflix~ Meh-flix 🙃 - Movie Recommender System Project
The project uses cosine similarity to make movie recommendations based on a user's genre selection(s). 

It also uses `KNNBaseline`'s `get_neighbors()` method to make recommendations based on a user's movie choice.

## Demo
You can test the app here: https://meh-flix.streamlit.app/

## How It Works
For the **content-based** aspect, all movies are mapped out to 18 dimensions with each dimension representing a unique genre. A value of '1' in a dimension indicates that a movie falls into that genre category and '0' indicates otherwise.

When a user selects their preferred genre combination, a pseudo-movie is created and it is also mapped out to the 18 dimensions with a '1' indicating a selected genre and '0' otherwise. 

After each selection, a cosine similarity score is calculated between the pseudo-movie and all the movies in the dataset. Then the top 10 movies with the highest score are recommended to the user.

For the **collaborative-filtering** aspect, 
## Relevant Materials
files necessary for app to run...
workspace where models were built...

## Possible Improvements
- Experiment with the use each movie's synopsis as features to build a content-based recommender system
- Experiment with more complex algorithms for collaborative filtering recommender system
