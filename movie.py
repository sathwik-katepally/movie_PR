class Movie:
    def __init__(self, movie_id, title, genre):
        self.id = movie_id
        self.title = title
        self.genre = genre
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

    def __str__(self):
        return f"Movie(id={self.id}, title='{self.title}', genre='{self.genre}', average_rating={self.get_average_rating():.2f})"
