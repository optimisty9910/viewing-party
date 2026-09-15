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

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

