# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_movies = user_data["watched"]
    friends = user_data["friends"]
    friends_movies = []
    unique_movies = []

    for friend in friends:
        friends_movies.extend(friend["watched"])

    for movie in user_movies:
        if movie not in friends_movies:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    user_movies = user_data["watched"]
    friends = user_data["friends"]
    friends_movies = []
    friends_unique_movies = []
    
    for friend in friends:
        friends_movies.extend(friend["watched"])

    seen_titles = set()
    unique_friends_movies = []
    for movie in friends_movies:
        title = movie["title"]
        if title not in seen_titles:
            seen_titles.add(title)
            unique_friends_movies.append(movie)

    for movie in unique_friends_movies:
        if movie not in user_movies:
            friends_unique_movies.append(movie)
    
    return friends_unique_movies



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

