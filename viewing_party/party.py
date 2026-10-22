# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # test case ["a", "b", 0] return ["a", "b", 0]
    if title and genre and rating is not None:
        return {
            "title": title,
            "genre": genre,
            "rating": rating
        }

    # test case ["a", "b", 0] return None
    # if title and genre and rating:
    #     return {
    #         "title": title,
    #         "genre": genre,
    #         "rating": rating
    #     }
    # return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# iteration may go wrong with remove()
def watch_movie(user_data, title):
    watched = user_data["watched"]
    watchlist = user_data["watchlist"]

    new_watchlist = []

    for movie in watchlist:
        if movie["title"] == title:
            watched.append(movie)
            continue
        else:
            new_watchlist.append(movie)

    user_data["watchlist"] = new_watchlist

    return user_data

# def watch_movie(user_data, title):
#     for movie in user_data["watchlist"]:
#         if movie["title"] == title:
#             user_data["watchlist"].remove(movie)
#             user_data["watched"].append(movie)
    
#     return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    """
    # avoid ZeroDivisionError
    if not user_data["watched"] or len(user_data["watched"] == 0):
        return 0.0
    """
    watched = user_data["watched"]
    
    if not watched or len(watched) == 0:
        return 0.0
    
    total_rating = 0

    for movie in watched:
        total_rating += movie["rating"]
    
    return total_rating / len(watched)

def get_most_watched_genre(user_data):
    watched = user_data["watched"]
    
    if not watched:
        return None
    
    genre_dict = {}
    for movie in watched:
        genre = movie["genre"]
        genre_dict[genre] = genre_dict.get(genre, 0) + 1
        
    sorted_genre = sorted(genre_dict.items(), key = lambda items: items[1])

    return sorted_genre[-1][0]      

# -----------------------------------------
# ------------- WAVE 3 --------------------

def get_friends_watched_no_duplicates(user_data):
    friends = user_data.get("friends", [])
    seen_titles = set()
    unique_friends_movies = []

    for friend in friends:
        for movie in friend.get("watched", []):
            title = movie.get("title")
            if title and title not in seen_titles:
                seen_titles.add(title)
                unique_friends_movies.append(movie)
    
    return unique_friends_movies

def get_unique_watched(user_data):
    user_movies = user_data["watched"]
    friends_movies = get_friends_watched_no_duplicates(user_data)
    unique_movies = []

    for movie in user_movies:
        if movie not in friends_movies:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    user_movies = user_data["watched"]
    friends_movies = get_friends_watched_no_duplicates(user_data)
    unique_friends_movies = []
    
    for movie in friends_movies:
        if movie not in user_movies:
            unique_friends_movies.append(movie)
    
    return unique_friends_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
def get_available_recs(user_data):
    unique_friends_movies = get_friends_unique_watched(user_data)
    subscriptions = user_data.get("subscriptions", [])

    recommendations = []

    for movie in unique_friends_movies:
        if movie["host"] in subscriptions:
            recommendations.append(movie)

    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------

def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    rec_movies = []
    friends_unique_watched = get_friends_unique_watched(user_data)

    if not friends_unique_watched:
        return []

    for movie in friends_unique_watched:
        if movie["genre"] == most_watched_genre:
            rec_movies.append(movie)

    return rec_movies

def get_rec_from_favorites(user_data):
    unique_movies = get_unique_watched(user_data)
    favorites = user_data["favorites"]
    rec_movies = []

    for movie in favorites:
        if movie in unique_movies:
            rec_movies.append(movie)

    return rec_movies
