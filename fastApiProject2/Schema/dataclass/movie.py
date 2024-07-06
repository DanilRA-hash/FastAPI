import datetime

from pydantic import BaseModel, Field
from schema2.enums import GenreEnum, LanguageEnum


class MovieBaseModel(BaseModel):
    name: str = Field(...,description="Name of the movie",max_length=30,min_length=3)
    genre: GenreEnum
    release_date: datetime.date
    rating: float = Field(...,lt = 10, gt =1,description="The rating of the movie")
    language: LanguageEnum

