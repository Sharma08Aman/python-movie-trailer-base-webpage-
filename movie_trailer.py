import webbrowser

class Movie():
    """ Class Movie is designed to assign class variables
    to their respective arguements for calling as follows
        self: its variable assigned to further call class globally by that arguement
        movie_title: it assigns to title of the movie
        movie_storyline: it assigns to the storyline of the movie
        poster_image: it assigns to url that has the movie poster
        trailer_youtube: it assigns to url that has trailer of the movie
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

#defining additional instance methods to
#open trailer and image
    def show_trailer(self):

        """ This instance method calls for
        the trailer of the movie to pop
        """
        webbrowser.open(self.trailer_youtube_url)
        
    def show_poster(self):
        """ This is an optional instance method
        that calls for poster of movie to pop
        """
        webbrowser.open(self.poster_image_url)
