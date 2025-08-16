from Library import Library

library = Library()


while True:
    try:

        print("1. Add book")
        print("2. Remove book")
        print("3. Load book")
        print("4. Save book")
        print("5. Display book")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:

            library.add_book()

        elif choice == 2:

            library.remove_book()

        elif choice == 3:

            library.load_book()

        elif choice == 4:

            library.save_book()

        elif choice == 5:

            library.display_books()

        else:
            break

    except ValueError:
        print("Invalid choice. Please try again.")
        continue



