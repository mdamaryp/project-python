from modules.library_item import LibraryItem


class Dvd(LibraryItem):
    def __init__(self, title, upc, subject, actor, director, genre):
        super().__init__(title, upc, subject)
        self.actor = actor
        self.director = director
        self.genre = genre
