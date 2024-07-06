from Data import movies_list, GenreEnum
from settings import initialize_db
from schema2 import MovieModel
from schema2.Models import LanguageEnum, GenreEnum

initialize_db()

movies = list(movies_list.values())
for movie in movies:
    print(movie)
    movie["language"] = LanguageEnum[movie["language"]]
    movie["genre"] = GenreEnum[movie["genre"]]
    MovieModel(**movie).save()