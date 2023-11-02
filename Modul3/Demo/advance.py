from functools import reduce

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

def highest_rated_movie(movies):
    highest_rated = max(movies, key=lambda x: x["rating"])
    return highest_rated

def show_rating_by_year(movies):
    def average_rating_by_year(year):
        movies_in_year = list(filter(lambda x: x["year"] == year, movies))
        total_ratings = reduce(lambda x, y: x + y["rating"], movies_in_year, 0)
        return total_ratings / len(movies_in_year) 
    years = map(lambda x: x["year"], movies)
    average_ratings = {year: average_rating_by_year(year) for year in years}
    return str(average_ratings)

def show_movies_by_genre(movies):
    def count_movies_by_genre(genre):
        return len(list(filter(lambda x: x["genre"] == genre, movies)))
    genres = map(lambda x: x["genre"], movies)
    genre_counts = {genre: count_movies_by_genre(genre) for genre in genres}
    return f"Jumlah Film berdasarkan genre: {genre_counts}"

def show_movie_data(movie_title, movies):
    selected_movie = list(filter(lambda x: x["title"] == movie_title, movies))
    if selected_movie:
        return str(*selected_movie)
    else:
        return "Tidak ada Film"


inputMenu = lambda menu: input(menu).lower() 
inputTitle = lambda title: input(title)
def main():
    while True:
        print("[1] Menghitung jumlah film berdasarkan genre \n[2] Menghitung rata-rata rating film berdasarkan tahun \n[3] Menemukan film dengan rating tertinggi \n[4] Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre \n[5] Selesai")
        result =  inputMenu("Pilih: ")
        if result == "1":
            print(show_movies_by_genre(movies) + "\n\n")
        elif result == "2":
            print(f"Rata-rata rating film berdasarkan tahun: {show_rating_by_year(movies)} \n\n")
        elif result == "3":
            print(f"Film rating tertinggi: {highest_rated_movie(movies)}\n\n")
        elif result == "4":
            title = inputTitle("Masukkan judul film: ")
            print(*show_movie_data(title, movies) + "\n\n")
        elif result == "5":
            exit()
        else:
            print("Pilihan tidak ada  \n\n")

if __name__ == "__main__":
    main()