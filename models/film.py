from .genre import Genre

class Film:

    def __init__(self, name: str, year: int, duration_in_minutes: float, genre: Genre, studio: str):
        self.name = name
        self.year = year
        self.duration_in_minutes = duration_in_minutes
        self.genre = genre
        self.studio = studio


    def __str__(self):
        return f'name: {self.name} \n' \
               f' year: {self.year} \n' \
               f' genre: {self.genre} \n' \
               f' studio: {self.studio} \n' \
               f' duration: {self.duration_in_minutes}\n'
