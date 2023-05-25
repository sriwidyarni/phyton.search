def is_similar(title1, title2) :
    title1 = title1.lower()
    title2 = title2.lower()

    if title1[0] == title2[0] :
        return True
    
    return False

def Sequential_search(books, book_title) :
    for book in books :
        if is_similar(book['title'], book_title) :
            return book['self']
        
    return "book tidak ditemukan"
books = [

    {'title': 'python programing', 'self': 'A1'},
    {'title': 'data structures and algorithms', 'self': 'B2'},
    {'title': 'introduction to machine learning', 'self': 'C3'},
    {'title': 'database management systems', 'self': 'D4'},
]

book_title = input("Masukan judul buku yang ingin dicari :")
self_location = Sequential_search(books, book_title)
print (self_location)