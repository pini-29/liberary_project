from data import books
def search_book(books, name):
    listi = []
    for book in books:
        if name in book["name"]:
            listi.append(book["name"])
            return listi
    return None

def add_book(books, name, author, year):
    booki = {"id": 0,"name":None,"author":None,"year":0,"available":True}
    if year < 0:
        raise ValueError("The year must be a positiv number")
    if not name:
        raise ValueError("Please enter the name of book")
    if not author:
        raise ValueError("Please enter the name of author")
    
    for book in books:
        if book["name"] == name and book["author"] == author:
            return "This book is alredy exists"
    id = len(books)
    booki["id"]= id + 1 
    booki["name"]=name
    booki["author"]=author
    booki["year"]=year
    books.append(booki)
    return "The addition was successful."

def borrow_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            if book["available"] == False:
                return "The book is alredy borrow"
            elif book["available"] == True:
                book["available"]=False
                return "You borrow the book"
    return "Please enter id true"

def return_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            if book["available"] == True:
                return "The book is alredy return"
            elif book["available"] == False:
                book["available"]=True
    return "You return the book"

def get_available_books(books):
    listi = []
    for b in books:
        if b["available"] == True:
            listi.append(b["name"])
    return listi

def get_books_by_author(books, author):
    listi = []
    for b in books:
        if b["author"] == author:
            listi.append(b["name"])
    return listi




    

        