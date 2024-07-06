from fastapi import FastAPI,HTTPException,status
from Data import movies_list
from Data import GenreEnum
from Schema.dataclass.movie import MovieBaseModel
from NEW.Models.movies import MovieModel
from settings import initialize_db
app = FastAPI()

initialize_db()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{roll_no}")
# async def say_hello(roll_no: int):
#     return {"message": f"Hello {roll_no}"}
#
# @app.get('/movies')
# async def get_all_movies():
#     return list(movies_list.values())
#
# @app.get('/movies/{movie_name}')
# async def get_the_movies(movie_name: str):
#     if movie_name not in movies_list:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Movie not found")
#     return movies_list[movie_name]
#
# @app.get("/movies/page")
# async def p(limit: int = 5):
#     all_movies = list(movies_list.values())
#     return all_movies[:limit]
#
# #async def g(offset: int, limit: int = 5):
#     #all_movies = list(movies_list.values())
#     #movies_count = len(all_movies)
#     #start_index = (offset - 1) * limit
#     #end_index = start_index + limit
#
#
# @app.get("/movies/page/{genre}")
# async def get_all_genre_movies(genre: GenreEnum):
#     all_movies = list(movies_list.values())
#     genre_movies = []
#     for movie in all_movies:
#         if movie["genre"] == genre.value:
#             genre_movies.append(movie)
#     return genre_movies
#
# @app.post("/movies")
# async def create_movies(movie: MovieBaseModel):
#     movies_list[movie.name] = movie.dict()
#     return {"message": f"Movie {movie.name} successfully created"}
#
# @app.delete("/movies/delete/{movie_name}")
# async def delete_movies(movie_name: str):
#     if movie_name not in movies_list:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Movie not found")
#     del movies_list[movie_name]
#     return {"message": f"Movie {movie_name} successfully deleted"}
#
#
#
# '''@app.put("/movies/put/{movie_name}")
# async def update_movies(movie: MovieBaseModel):
#     if movie.movie_name not in movies_list:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Movie not found")
#     movies_list[movie.movie_name] = movie.model_dump()
#     return {"message": f"Movie {movie.name} successfully updated"}'''
#
#
#

@app.get("/movies")
async def get_all_movies():
    movies_list = MovieModel.objects.all()
    response_list = []
    for movie in movies_list:
        response_list.append(
        MovieBaseModel(name = movie.name, rating = movie.rating,release_date = movie.release_date, genres = movie.genres,language = movie.language)
        )
    return response_list


@app.post("/create_movie/")
async def create_movie(new_movie: MovieBaseModel):
    movie = MovieModel(**new_movie.model_dump())
    movie.save()
    return {"message": f"Movie {movie.name} has been created"}

