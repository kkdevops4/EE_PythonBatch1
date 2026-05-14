users = []
books = [
    {"id": 1, "title": "Harry Potter", "author": "Rowling", "genre": "Fantasy", "available": True, "user": ""},
    {"id": 2, "title": "Hobbit", "author": "Tolkien", "genre": "Fantasy", "available": True, "user": ""},
    {"id": 3, "title": "Atomic Habits", "author": "James", "genre": "Self Help", "available": True, "user": ""},
    {"id": 4, "title": "1984", "author": "Orwell", "genre": "Classic", "available": True, "user": ""},
    {"id": 5, "title": "Sapiens", "author": "Harari", "genre": "History", "available": True, "user": ""},
    {"id": 6, "title": "Alchemist", "author": "Coelho", "genre": "Fiction", "available": True, "user": ""},
    {"id": 7, "title": "Ikigai", "author": "Garcia", "genre": "Self Help", "available": True, "user": ""},
    {"id": 8, "title": "Rich Dad", "author": "Kiyosaki", "genre": "Finance", "available": True, "user": ""},
    {"id": 9, "title": "Mockingbird", "author": "Lee", "genre": "Classic", "available": True, "user": ""},
    {"id": 10, "title": "Think Rich", "author": "Hill", "genre": "Self Help", "available": True, "user": ""}
]

def add_user():
    users.append({"id": input("User id: "), "name": input("Name: ")})
    print("User added")

def borrow_book():
    b = int(input("Book id: "))
    u = input("User id: ")
    for book in books:
        if book["id"] == b:
            if book["available"]:
                book["available"] = False
                book["user"] = u
                print("Borrowed")
            else:
                print("Already borrowed")

def return_book():
    b = int(input("Book id: "))
    for book in books:
        if book["id"] == b:
            if not book["available"]:
                book["available"] = True
                book["user"] = ""
                print("Returned")

def search():
    c = input("1.Author 2.Genre 3.ID: ")

    if c == "3":
        b = int(input("ID: "))
        for book in books:
            if book["id"] == b:
                print(book["id"], book["title"], "(Available)" if book["available"] else "(Borrowed by ID " + book["user"] + ")")

        return

    v = input("Enter: ").lower()

    print("\nAvailable:")
    for book in books:
        if book["available"] and ((c=="1" and v in book["author"].lower()) or (c=="2" and v in book["genre"].lower())):
            print(book["id"], book["title"])

    print("\nBorrowed:")
    for book in books:
        if not book["available"] and ((c=="1" and v in book["author"].lower()) or (c=="2" and v in book["genre"].lower())):
            print(book["id"], book["title"], "-", book["user"])


def show():
    for b in books:
        print(b["id"], b["title"], "(Available)" if b["available"] else "(Borrowed)")

while True:
    print("\n1.Add User 2.Borrow 3.Return 4.Search 5.Show 6.Exit")
    ch = input("Choice: ")

    if ch == "1": add_user()
    elif ch == "2": borrow_book()
    elif ch == "3": return_book()
    elif ch == "4": search()
    elif ch == "5": show()
    elif ch == "6": break
