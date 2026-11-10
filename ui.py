import data
def show_menu():
    print("================================")
    print("LIBRARY MANAGEMENT")
    print("================================")
    print("1. Display all books")
    print("2. Search book by name")
    print("3. Add new book")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Display available books")
    print("7. Display books by author")
    print("8. Exit")
    
    print("Choose an option:")

def display_books(books):
     for dicti in books: 
         print( f"The book is {dicti["name"]}")




