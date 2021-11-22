import fresh_tomatoes

import movie_trailer

#creating instances for vaious movies
toy_story= movie_trailer.Movie("Toy story",
                               "Story of a boy and his toys coming to life",
                               "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                               "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

avatar= movie_trailer.Movie("Avatar",
                            "A marine stranded as alien",
                            "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                            "https://www.youtube.com/watch?v=5PSNL1qE6VY")

alita_battle_angel= movie_trailer.Movie("Alita Battle Angel", 
                                       "Ä cyborg girl finding her humanity and purpose", 
                                       "https://en.wikipedia.org/wiki/File:Alita_Battle_Angel_(2019_poster).png", 
                                       "https://www.youtube.com/watch?v=w7pYhpJaJW8")

angry_birds= movie_trailer.Movie("Angry Bird",
                                "Angry birds retaliating on pigs",
                                "https://upload.wikimedia.org/wikipedia/en/f/f9/The_Angry_Birds_Movie_poster.png", 
                                "https://www.youtube.com/watch?v=QRmKa7vvct4")

avengers= movie_trailer.Movie("Avengers",
                             "A Group of superheroes protecting earth",
                             "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                             "https://www.youtube.com/watch?v=eOrNdBpGMv8")

wasseypur= movie_trailer.Movie("Gangs of wasseypur",
                              "War between two group of thugs and their families",
                              "https://upload.wikimedia.org/wikipedia/en/6/6a/Gangs_of_Wasseypur_poster.jpg", 
                              "https://www.youtube.com/watch?v=j-AkWDkXcMY")

#creating list of movies with instances created
movies=[toy_story,avatar,alita_battle_angel,angry_birds,avengers,wasseypur]

#calling fresh_tomatoes created module for opening movie in webpage style
fresh_tomatoes.open_movies_page(movies)



                                    
