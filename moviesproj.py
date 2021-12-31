MENU_PROMPT  = "\nEnter 'a' to add a movie, 'v' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []  #List of dictionaries

# Appending each movie as dictionaries
# dictionary with 3 keys: title, director and year
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    
    movies.append({
        "title": title,
        "director": director,
        "year": year
    })


def show_movie(movies_list):
    for movie in movies_list:
        print_movie(movie)


# mov new variable that gets created when this function runs     
def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']} ")


# Goes through the movie list 
def find_movie():
    find_by = input("What property of the movie are you looking for? ") # one of year,title or director
    looking_for = input("What are you searching for? ")
    #for whatever we find that matches the abovementioned attributes, we add it to the list below
    found_movies = find_by_attributes(movies, looking_for, lambda x: x[find_by])
    #'expected' value is the 'looking_for' value
    #'finder' value is a lambda x: x[find_by]  where 
    # its taking in a parameter and returning a find by key of the parameter
    show_movie(found_movies)


def find_by_attributes(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:     
            found.append(i)
            
    return found

"""
Making an improvement to our menu using first-class 
functions. All functions in Python are first-class functions
in menu function, there is a 'if' statement for each 
different option that a user can type and this is ok
if you have only 3-4 options available.
But if you have 10 options, then it can become a bit unwieldy.
"""

"""
Defining a user dictionary
"""
# user_options = {
#     "a": add_movie,
#     "v": show_movie,
#     "f": find_movie,   
# }

# def menu():
#     selection = input(MENU_PROMPT)
#     while selection != 'q':
#         if selection in user_options:
#             selected_functions = user_options[selection]
#             selected_functions() #run a function by putting in brackets; first class functions property
#         else:
#             print('Unknown command.Please try again.')
#         selection = input(MENU_PROMPT)


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'a':
            add_movie()
        elif selection == 'v':
            show_movie(movies)
        elif selection == 'f':
            find_movie()
        else:
            print('Unknown command.Please try again.')


        selection = input(MENU_PROMPT)

# Remember to run the user menu function at the end!
menu()



