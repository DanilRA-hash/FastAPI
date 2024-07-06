import os

import mongoengine


def initialize_db() -> None:
    mongoengine.connect(host="mongodb://localhost:27017/",db="netflix")