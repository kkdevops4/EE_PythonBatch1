
# Library Book Manager - Mini Project
from datetime import date, timedelta
import time

users = []
books = []

def thank_you_and_wait():
    print("\n" + "=" * 45)
    print(" Thank you!")
    print("Returning to main menu in 5 seconds...")
    print("=" * 45)
    time.sleep(5)



def load_books():
    global books
    books = [
        {"book_id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "genre": "Fantasy",
         "is_available": True, "borrowed_by": None, "borrow_date": None, "return_date": None},
        {"book_id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy",
         "is_available": True, "borrowed_by": None, "borrow_date": None, "return_date": None},
        {"book_id": 3, "title": "Atomic Habits", "author": "James Clear", "genre": "Self Help",
         "is_available": True, "borrowed_by": None, "borrow_date": None, "return_date": None},
        {"book_id": 4, "title": "Think and Grow Rich", "author": "Napoleon Hill", "genre": "Self Help",
         "is_available": True, "borrowed_by": None, "borrow_date": None, "return_date": None},
        {"book_id": 5, "title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fiction",
         "is_available": True, "borrowed_by": None, "borrow_date": None, "return_date": None},
        {"book_id": 6, "title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "genre": "Finance",
         "is_available": True, "borrowed_by": None, "borrow_date": None, "return_date": None},
        {"book_id": 7, "title": "1984", "author": "George Orwell", "genre": "Classic",
         "is_available": True, "borrowed_by": None, "borrow_date": None, "return_date": None},
        {"book_id": 8, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Classic",
         "is_available": True, "borrowed_by": None, "borrow_date": None, "return_date": None},
        {"book_id": 9, "title": "Ikigai", "author": "Hector Garcia", "genre": "Self Help",
         "is_available": True, "borrowed_by": None, "borrow_date": None, "return_date": None},
        {"book_id": 10, "title": "Sapiens", "author": "Yuval Noah Harari", "genre": "History",
         "is_available": True, "borrowed_by": None, "borrow_date": None, "return_date": None},
        
    ]



def add_user():
    user_id = input("Enter User ID: ")
    name = input("Enter User Name: ")

    users.append({"user_id": user_id, "name": name})
    print(" User added successfully.")
    thank_you_and_wait()

def get_user(user_id):
    for user in users:
        if user["user_id"] == user_id:
            return user
    return None



def borrow_book():
    if not users:
        print(" No users registered.")
        print("Please add a user before borrowing a book.")
        thank_you_and_wait()
        return

    try:
        book_id = int(input("Enter Book ID (1-20): "))
    except ValueError:
        print(" Invalid input. Enter a number.")
        thank_you_and_wait()
        return

    book = next((b for b in books if b["book_id"] == book_id), None)

    if not book:
        print(" Invalid Book ID.")
        thank_you_and_wait()
        return

    if not book["is_available"]:
        print(" Book already borrowed.")
        thank_you_and_wait()
        return

    user_id = input("Enter User ID: ")
    user = get_user(user_id)

    if not user:
        print(" User not found. Please add user first.")
        thank_you_and_wait()
        return

    today = date.today()
    return_date = today + timedelta(days=7)

    book["is_available"] = False
    book["borrowed_by"] = user_id
    book["borrow_date"] = today
    book["return_date"] = return_date

    print("\n Book Borrowed Successfully")
    print(f"Book ID     : {book['book_id']}")
    print(f"Title       : {book['title']}")
    print(f"Author      : {book['author']}")
    print(f"Genre       : {book['genre']}")
    print(f"Borrow Date : {today}")
    print(f"Return Date : {return_date}")

    thank_you_and_wait()



def search_books():
    print("\n All Books:")
    for book in books:
        status = "Available " if book["is_available"] else "Borrowed "
        print(f"{book['book_id']} - {book['title']} ({status})")

    print("\nSearch By:")
    print("1. Author")
    print("2. Genre")
    print("3. Book ID")
    print("4. Back to Menu")

    choice = input("Enter choice: ")

    if choice == "4":
        return

    if choice == "3":
        try:
            book_id = int(input("Enter Book ID: "))
        except ValueError:
            print(" Invalid ID.")
            thank_you_and_wait()
            return

        book = next((b for b in books if b["book_id"] == book_id), None)

        if not book:
            print(" Book not found.")
        else:
            if book["is_available"]:
                print("\n Book Found (Available)")
                print(f"Book ID : {book['book_id']}")
                print(f"Title   : {book['title']}")
                print(f"Author  : {book['author']}")
                print(f"Genre   : {book['genre']}")
                print("Status  : Available ")
            else:
                user = get_user(book["borrowed_by"])
                print("\n Book Found (Borrowed)")
                print(f"Book ID     : {book['book_id']}")
                print(f"Title       : {book['title']}")
                print(f"Author      : {book['author']}")
                print(f"Genre       : {book['genre']}")
                print(f"Borrowed By : {user['name']}")
                print(f"Borrow Date : {book['borrow_date']}")
                print(f"Return Date : {book['return_date']}")

        thank_you_and_wait()
        return

   
    value = input("Enter search value: ").lower()
    found = False

    print("\nSearch Results:")
    for book in books:
        if (choice == "1" and book["author"].lower() == value) or \
           (choice == "2" and book["genre"].lower() == value):
            status = "Available " if book["is_available"] else "Borrowed"
            print(f"{book['book_id']} - {book['title']} ({status})")
            found = True

    if not found:
        print(" No matching books found.")

    thank_you_and_wait()



def main():
    load_books()

    while True:
        print("\n=================================")
        print("      LIBRARY BOOK MANAGER     ")
        print("=================================")
        print("1. Add User")
        print("2. Borrow Book")
        print("3. Search Book")
        print("4. Exit")
        print("=================================")

        choice = input("Enter choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            search_books()
        elif choice == "4":
            print("\n Thank you for using Library Book Manager!")
            break
        else:
            print(" Invalid choice.")
            thank_you_and_wait()



if __name__ == "__main__":
    main()