1. All ratings are contained in the file "ratings.dat" and are in the
following format:

UserID::MovieID::Rating::Timestamp

- UserIDs range between 1 and 6040 
- MovieIDs range between 1 and 3952
- Ratings are made on a 5-star scale (whole-star ratings only)
- Timestamp is represented in seconds since the epoch as returned by time(2)
- Each user has at least 20 ratings




2. Movie information is in the file "movies.dat" and is in the following
format:

MovieID::Title::Genres

- Titles are identical to titles provided by the IMDB (including
year of release)
- Genres are pipe-separated and are selected from the following genres:

	* Action
	* Adventure
	* Animation
	* Children's
	* Comedy
	* Crime
	* Documentary
	* Drama
	* Fantasy
	* Film-Noir
	* Horror
	* Musical
	* Mystery
	* Romance
	* Sci-Fi
	* Thriller
	* War
	* Western

- Some MovieIDs do not correspond to a movie due to accidental duplicate
entries and/or test entries
- Movies are mostly entered by hand, so errors and inconsistencies may exist





3. Links Data File Structure (links.csv)
---------------------------------------

Identifiers that can be used to link to other sources of movie data are contained in the file `links.csv`. Each line of this file after the header row represents one movie, and has the following format:

    movieId,imdbId,tmdbId

movieId is an identifier for movies used by <https://movielens.org>. E.g., the movie Toy Story has the link <https://movielens.org/movies/1>.

imdbId is an identifier for movies used by <http://www.imdb.com>. E.g., the movie Toy Story has the link <http://www.imdb.com/title/tt0114709/>.

tmdbId is an identifier for movies used by <https://www.themoviedb.org>. E.g., the movie Toy Story has the link <https://www.themoviedb.org/movie/862>.






4. "movie_comp.csv" contains data scraped from each movie's (in "movie.dat") IMDb page. To find a given movie's IMDb homepage, replace "{imdbid}" in the following URL with the movie's actual IMDb ID: https://www.imdb.com/title/tt{imdbid}. For example, a movie with an IMDb ID of '0113497' has its IMDb homepage at "https://www.imdb.com/title/tt0113497/" 

These are the columns contained in "movie_comp.csv":

imdbId: a movie's unique IMDb ID
title: The title scraped from the IMDB site
image: URL of the image of the movie
year: the year the movie was produced as specified on its IMDB page
plot: the summary of the movie on its home page
directors: list of directors credited on the homepage (max. length of list =3)
writers: list of writers credited on the homepage (max. length of list =3)
top_cast: list of actors listed on the homepage (max. length of list = 18)