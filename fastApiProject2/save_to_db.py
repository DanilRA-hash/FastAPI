from Data import movies_list
from settings import initialize_db
from NEW.Models import MovieModel
from NEW.enums import LanguageEnum, GenreEnum

initialize_db()

movies = list(movies_list.values())
for movie in movies:
    print(movie)
    #movie["language"] = LanguageEnum[movie["language"]]
    #movie["genre"] = GenreEnum[movie["genre"]]
    MovieModel(**movie).save()