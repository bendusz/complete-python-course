MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movie_store = [
    {'title': 'Matrix', 'director': ' Lana Wachowski', 'release': int(1999)},
    {'title': 'Midnight in Paris', 'director': 'Woody Alen', 'release': int(2011)},
    {'title': 'Lego: The Movie', 'director': 'Phil Lord', 'release': int(2014)},
    {'title': 'Lassie', 'director': 'Charles Sturridge', 'release': int(2004)}
]


def add():
    movie = {'title': input("Please enter the title of the movie\n"),
             'director': input('Please enter the director of the movie\n'),
             'release': int(input('Please enter the year the movie was released\n'))}

    movie_store.append(movie)


def listing():
    for film in movie_store:
        print('Title: ' + film['title'] + '  Director: ' + film['director'] + '  Release year: ' + str(film['release']))


def find():
    what = input("Which movie are you looking for?\n")
    for film in movie_store:
        if what == film['title']:
            print('Title: ' + film['title'] + '  Director: ' + film['director'] + '  Release year: ' + str(
                film['release']))


while True:
    var = input(MENU_PROMPT)
    if var == 'a':
        add()
    elif var == 'l':
        listing()
    elif var == "f":
        find()
    elif var == "q":
        break
    else:
        print('Invalid option, please try again')
