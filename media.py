import webbrowser


class Movie():
    """This class provides a way to store movie related information.

        Attributes:
            movie_title (string): The title of the movie_title.
            movie_storyline (string): A one (or two) sentence
                summary of the plot.
            poster_image (string): A link for the poster of the movie,
                alternative posters are cool.
            trailer_youtube (string): The youtube URL for the movie's trailer.
            release_date (string): The release date of the movie
                (DD Month YYYY, because I like it this way).
            length (string): Duration of the movie, in minutes.
            director (string): The director.
            writer (string): The writer.
            producer (string): The executive producer.
            actors (string): The lead actors
    """

    VALID_RATINGS = ["G", "PG", "P-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, release_date, length,
                 director, writer, producer, actors):
        """Inits Movie class with basic information."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.length = length
        self.director = director
        self.writer = writer
        self.producer = producer
        self.actors = actors
        self.release_date = release_date

    # open a webbrowser and play the movie's trailer via youtube
    def show_trailer(self):
        """Plays the movie's trailer in a new browser window"""
        webbrowser.open(self.trailer_youtube_url)
