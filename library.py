from movie import Movie

class MovieLibrary:
    def __init__(self):
        self.movies = []
        self.next_id = 1

    def add_movie(self, title, genre):
        movie = Movie(self.next_id, title, genre)
        self.movies.append(movie)
        self.next_id += 1

    def rate_movie(self, movie_id, rating):
        #Implement the function

    def get_top_rated_movies(self, n):
        #Implement the function
        

# Main code
if __name__ == "__main__":
    library = MovieLibrary()
    library.add_movie("The Shawshank Redemption", "Drama")
    library.add_movie("The Godfather", "Crime")

    library.rate_movie(1, 9)
    library.rate_movie(1, 10)
    library.rate_movie(2, 10)
    library.rate_movie(2, 9)
    library.rate_movie(2, 8)

    print("Top rated movies:")
    top_movies = library.get_top_rated_movies(2)
    for movie in top_movies:
        print(movie)
