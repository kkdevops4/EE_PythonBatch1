# Movie rating tracker - Add movies with genre and year, find top-rated per decade, and compute average rating per genre.

movies = [
    {"name": "3 Idiots", "genre": "Comedy", "year": 2009, "rating": 8.4},
    {"name": "Dangal", "genre": "Sports", "year": 2016, "rating": 8.3},
    {"name": "Gully Boy", "genre": "Music", "year": 2019, "rating": 8.0},
    {"name": "Kabir Singh", "genre": "Romance", "year": 2019, "rating": 7.1},
    {"name": "PK", "genre": "Comedy", "year": 2014, "rating": 8.1},
    {"name": "Lagaan", "genre": "Drama", "year": 2001, "rating": 8.1}
]

def add_movie():
    name = str(input("Enter movie name: "))
    genre = str(input("Enter genre: "))
    year = int(input("Enter year: "))
    rating = float(input("Enter rating: "))
    
    movies.append({
        "name": name,
        "genre": genre,
        "year": year,
        "rating": rating
    })

def top_rated_per_decade():
    decades = {}

    for movie in movies:
        decade = (movie["year"] // 10) * 10

        if decade not in decades:
            decades[decade] = movie
        else:
            if movie["rating"] > decades[decade]["rating"]:
                decades[decade] = movie

    print("Top-rated movies per decade:")
    for d in decades:
        print("decade = ", d, ",", "movie = ", decades[d]["name"], ",", "rating = ", decades[d]["rating"])

def avg_rating_per_genre():
    totals = {}
    counts = {}

    for movie in movies:
        genre = movie["genre"]

        if genre not in totals:
            totals[genre] = movie["rating"]
            counts[genre] = 1
        else:
            totals[genre] += movie["rating"]
            counts[genre] += 1

    print("Average rating per genre:")
    for genre in totals:
        avg = totals[genre] / counts[genre]
        print(genre, ":", (avg))


while True:
    print("1. Add Movie")
    print("2. Show Top Rated per Decade")
    print("3. Show Average per Genre")
    print("4. All Movies")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_movie()
    elif choice == "2":
        top_rated_per_decade()
    elif choice == "3":
        avg_rating_per_genre()
    elif choice == "4":
        for movie in movies:
            print(movie["name"])
    elif choice == "5":
        break
    else:
        print("Invalid choice")