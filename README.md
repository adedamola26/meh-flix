# ~Nefflix~ Meh-flix 🙃 - Movie Recommender System Project
The project uses cosine similarity to make movie recommendations based on a user's genre selection(s). 

It also uses `KNNBaseline`'s `get_neighbors()` method to make recommendations based on a user's movie choice.

## Demo
You can test the app here: https://meh-flix.streamlit.app/

## How It Works
For the **content-based** aspect, all movies are mapped out to 18 dimensions with each dimension representing a unique genre. A value of '1' in a dimension indicates that a movie falls into that genre category and '0' indicates otherwise.

When a user selects their preferred genre combination, a pseudo-movie is created and it is also mapped out to the same 18 dimensions with a '1' indicating a selected genre and '0' otherwise. 

After each selection, a cosine similarity score is calculated between the pseudo-movie and each movie in the dataset. Then the top 10 movies with the highest scores are recommended to the user.

For the **collaborative-filtering** aspect, after performing some hyperparameter tuning on KNNBaseline, we trained an item-based model on our dataset. The model's `get_neighbors()` method is responsible for returning the _k_ movies with the highest pearson baseline similarity score.

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
  
**For an EDA of the dataset and hyperparameter tuning for KNNBaseline**

Click me

**For the content based aspect**

Click me
## Possible Improvements
- Experiment with the use of each movie's synopsis/summary as features to build a content-based recommender system
- Experiment with more complex algorithms for collaborative filtering recommender system
