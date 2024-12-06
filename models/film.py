from datetime import datetime
from bson import ObjectId


class Film:
    def __init__(self, title, release_date, director, planets=None):
        self.title = title
        self.release_date = release_date
        self.director = director
        self.planets = planets or []
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            "title": self.title,
            "release_date": self.release_date,
            "director": self.director,
            "planets": self.planets,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @staticmethod
    def from_dict(data):
        film = Film(
            title=data["title"],
            release_date=data["release_date"],
            director=data["director"],
            planets=data.get("planets", [])
        )
        if "created_at" in data:
            film.created_at = data["created_at"]
        if "updated_at" in data:
            film.updated_at = data["updated_at"]
        return film