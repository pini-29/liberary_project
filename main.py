from data import books
from ui import show_menu,display_books
import logic

def main():
    while True:
        show_menu()
        choice = input("Enter your choice")
        if choice == "1":
           print("hi")
           display_books(books)
        if choice == "2":
            name = input("Enter the name of book")
            a = logic.search_book(books,name)
            print(a)
        if choice == "3":
            
            namei = input("Enter the name of book")
            author = input("Enter the name if author")

            try:
               year = int(input("Enter the year"))
            except ValueError:
                print("You have a mistake")
            b = logic.add_book(books,namei,author,year)
            print(b)
        if choice == "4":
            book_id = int(input("Enter the book id do you whant to borrow"))
            borrow = logic.borrow_book(books,book_id)
            print(borrow)
        if choice == "5":
            ret_book_id = input("Enter the book id do you whant return")
            ret = logic.return_book(books,ret_book_id)
            print(ret)
        if choice == "6":
            r = logic.get_available_books(books)
            print(r)
        if choice == "7":
            input_author = input("Enter the author name")
            books_author = logic.get_books_by_author(books,input_author)
            print(books_author)
        if choice == "8":
            break

        


if __name__ == "__main__":
      main()