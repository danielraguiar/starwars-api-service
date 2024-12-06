from datetime import datetime
from bson import ObjectId


class Planet:
    def __init__(self, name, climate, diameter, population, films=None):
        self.name = name
        self.climate = climate
        self.diameter = diameter
        self.population = population
        self.films = films or []
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            "name": self.name,
            "climate": self.climate,
            "diameter": self.diameter,
            "population": self.population,
            "films": self.films,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @staticmethod
    def from_dict(data):
        planet = Planet(
            name=data["name"],
            climate=data["climate"],
            diameter=data["diameter"],
            population=data["population"],
            films=data.get("films", [])
        )
        if "created_at" in data:
            planet.created_at = data["created_at"]
        if "updated_at" in data:
            planet.updated_at = data["updated_at"]
        return planet