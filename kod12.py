class Book:
    pages_num = 250
    genre = "sci-fi"
    critics_score = "7.8/10"
    publisher = "XYZ"
    catalog_num = 239183


book1 = Book()
print(book1)
print(book1.publisher)
book1.publisher = "ABC"
print(book1.publisher)
