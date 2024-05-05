# ~Nefflix~ Meh-flix 🙃 - Movie Recommender System Project
The project uses cosine similarity to make movie recommendations based on a user's genre selection(s). 

It also uses `KNNBaseline`'s `get_neighbors()` method to make recommendations based on a user's movie choice.

## Demo
You can test the app here: https://meh-flix.streamlit.app/

## How It Works
For the **content-based** aspect, each movie is represented in an 18-dimensional space, with each dimension corresponding to a unique genre. A value of '1' in a dimension signifies the presence of that genre in the movie, while '0' indicates its absence.

When a user selects their preferred genre combination, a pseudo-movie is created and similarly represented in the 18-dimensional space with a '1' indicating a selected genre and '0' otherwise. 

Following each selection, a cosine similarity score is computed between the pseudo-movie and every movie in the dataset. Subsequently, the top 10 movies with the highest scores are recommended to the user.

For the **collaborative-filtering** aspect, after performing some hyperparameter tuning on KNNBaseline, we trained an item-based model on our dataset. The model's `get_neighbors()` method is responsible for returning the _k_ movies with the highest Pearson baseline similarity score.

## Relevant Materials
**To run the app locally**:
- Clone the repository
- Install dependencies using:
  ```
  pip install -r requirements.txt
  ```
- Run the following command:
  ```
  streamlit run Introduction.py
  ```
  
**For an EDA of the dataset and hyperparameter tuning for KNNBaseline**,

[Click me](lab/collabfiltering%20experiments.ipynb)

**For the content based aspect and extended collaborative filtering work**,

[Click me](lab/meh-flix%20workspace.ipynb)
## Possible Improvements
- Experiment with the use of each movie's synopsis/summary as features to build a content-based recommender system
- Experiment with more complex algorithms for collaborative filtering recommender system
