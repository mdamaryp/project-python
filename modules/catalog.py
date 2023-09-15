from modules.library_item import LibraryItem
from modules.book import Book
from modules.magazine import Magazine
from modules.cd import Cd
from modules.dvd import Dvd


class Catalog():
    def __init__(self, catalog=None):
        self.catalog = catalog

    def search(self, input_search):
        list_result = []
        for catalog in self.catalog:
            for item in catalog:
                if input_search.lower() in item.title.lower():
                    if type(item) == Book:
                        list_result.append(
                            f'Title :  {item.title}, type catalog : Book')
                    elif type(item) == Magazine:
                        list_result.append(
                            f'Title :  {item.title}, type catalog : Magazine')
                    else:
                        pass
        return list_result
