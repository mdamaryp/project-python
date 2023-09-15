from modules.library_item import LibraryItem
from modules.book import Book
from modules.magazine import Magazine
from modules.cd import Cd
from modules.dvd import Dvd
from modules.catalog import Catalog
import json

# item = LibraryItem('Judul 1', None,  'deskripsi judul 1')
# print(item.title)

# book = Book('isbn', 'Authors', 'title book', 'subject', 'dds_number', 'upc')
# print(book.title)

# book = Cd('Judul 1', None,  'deskripsi judul 1', 'artis')
# print(book.artist)

# book = Dvd('Judul 1', None,  'deskripsi judul 1', '1', '2', '3')
# print(book.genre)

r = open('files/data.json')
data_json = json.load(r)
# print(data_json)

list_book = []
list_magazine = []
list_dvd = []
list_cd = []


for item in data_json:
    if item['source'] == 'book':
        list_book.append(Book(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            isbn=item['issbn'],
            authors=item['authors'],
            dds_number=item['dds_number']
        ))
    elif item['source'] == 'magazine':
        list_book.append(Magazine(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            volume=item['volume'],
            issue=item['issue']
        ))
    elif item['source'] == 'dvd':
        list_book.append(Dvd(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            actor=item['actors'],
            director=item['directors'],
            genre=item['genre']
        ))
    elif item['source'] == 'cd':
        list_book.append(Cd(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            artist=item['artist']
        ))

catalog_all = [list_book, list_magazine, list_dvd, list_cd]

input_search = 'test'
result = Catalog(catalog_all).search(input_search)

print('=====| result |=====')
for index, result in enumerate(result):
    print(f'result ke - {index+1} | {result}')
