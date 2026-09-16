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
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0
    total_rating = 0
    number_of_movie = 0
    for movie in user_data["watched"]:
        total_rating += movie["rating"]
        number_of_movie += 1
    return total_rating / number_of_movie


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    genre_count = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre not in genre_count:
            genre_count[genre] = 1
        else:
            genre_count[genre] += 1
    sorted_genre = sorted(genre_count.items(), key = lambda items: items[1])        

    return sorted_genre[-1][0]      



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
