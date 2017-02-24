import fresh_tomatoes

import media

# Create movie objects
batman = media.Movie(
    "The Dark Knight",
    "When the menace known as the Joker wreaks havoc and chaos on the people "
    "of Gotham, the caped crusader must come to terms with one of the greatest"
    " psychological tests of his ability to fight injustice.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg",  # NOQA
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

toy_story = media.Movie(
    "Toy Story",
    "Andy's favourite toy, Woody, is worried that after Andy receives his "
    "birthday gift, a new toy called Buzz Lightyear, his importance may get "
    "reduced. He thus hatches a plan to eliminate Buzz.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",  # NOQA
    "https://www.youtube.com/watch?v=Bj4gS1JQzjk")

rang_de_basanti = media.Movie(
    "Rang De Basanti",
    "When Sue selects a few students to portray various Indian freedom "
    "fighters in her film, she unwittingly awakens their patriotism. The "
    "emotional and mental process turns them into rebels for a cause.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/RDB_poster.jpg/220px-RDB_poster.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=Dms-mPxc1SU")

avatar = media.Movie(
    "Avatar",
    "Marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

forrest_gump = media.Movie(
    "Forrest Gump",
    "American comedy-drama film based on the 1986 novel of the same name by "
    "Winston Groom",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=uPIEn0M8su0")

moana = media.Movie(
    "Moana",
    "Moana sets sail in search of Maui, a legendary demigod, in hopes to save "
    "her people",
    "https://upload.wikimedia.org/wikipedia/en/thumb/2/26/Moana_Teaser_Poster.jpg/220px-Moana_Teaser_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=LKFuXETZUsI")


movies_list = [batman, toy_story, rang_de_basanti, avatar, forrest_gump, moana]


# fresh_tomatoes module creates webpage to display movies list.
fresh_tomatoes.open_movies_page(movies_list)
