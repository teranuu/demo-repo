from Book import Book


class Library:

    def __init__(self):
        self.books = []


    def load_book(self):

        try:
            with open("library.txt", "r") as loadfile:
                for line in loadfile:
                    line = line.strip() #clear whitespaces, leaving only character strings
                    if line: #for each existing character string in a line (skipping empty lines)
                        parts = line.split(',') #splits the strings through comma as delimiter
                        if len(parts) == 3: #checks and assures parts can only have 3 variables
                            title, author, year = parts #unpacks parts into 3 separate variables
                            self.books.append(Book(title,author,year)) #packs the variables into the book object, then adds the object into the list

        except FileNotFoundError:
            print("Library file not found!")
            self.books = []


    def save_book(self):
        with open("library.txt", "w") as savefile:
            for book in self.books:
                savefile.write(f"{book.title},{book.author},{book.year}\n")


    def add_book(self):
        from Book import Book

        title = str(input("Enter book title: "))
        author = str(input("Enter book author: "))
        year = str(input("Enter book year: "))
        book = Book(title, author, year)

        if isinstance(book, Book):
            self.books.append(book)
            print("Book added!")

        else:
            print(f"Only Book instances can be added.")


    def remove_book(self):

        print("Available books: ")
        self.display_books()
        title = str(input("Enter book title to remove (type \"cancel\" to cancel): "))
        if title.lower() == "cancel":
            return

        if not self.books:
                print("There are no books to remove!")
                return

        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Removed book {title}.")
                return
        print("Book not found.")

    def display_books(self):
        print("Available books: ")
        if not self.books:
            print("None")
        else:

            for i, book in enumerate(self.books):
                print(f"{i + 1}.) {book}")


