import webbrowser


class Movie():
    """ Movie to store title, image, trailer, summary
    Attributes:
        title (str): movie title.
        storyline (str): summary of movie.
        poster_image_url (str): movie poster.
        trailer_youtube_url (str): movie trailer.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Show youtube movie trailer."""
        webbrowser.open(self.trailer_youtube_url)
