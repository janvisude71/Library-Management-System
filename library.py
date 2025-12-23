class Library:
    def __init__(self):
        self.file = "library.txt"

    def add_book(self):
        book_id = input("Enter Book ID: ")
        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        status = "Available"

        with open(self.file, "a") as f:
            f.write(f"{book_id}|{name}|{author}|{status}\n")
        print("Book added successfully!")

    def view_books(self):
        try:
            with open(self.file, "r") as f:
                books = f.readlines()
                if not books:
                    print("No books available.")
                    return
                print("\nID | Name | Author | Status")
                print("-" * 40)
                for book in books:
                    print(book.strip())
        except FileNotFoundError:
            print("Library file not found.")

    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")
        updated = []
        found = False

        with open(self.file, "r") as f:
            for line in f:
                data = line.strip().split("|")
                if data[0] == book_id and data[3] == "Available":
                    data[3] = "Issued"
                    found = True
                updated.append("|".join(data))

        with open(self.file, "w") as f:
            for line in updated:
                f.write(line + "\n")

        if found:
            print("Book issued successfully!")
        else:
            print("Book not available or not found.")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")
        updated = []
        found = False

        with open(self.file, "r") as f:
            for line in f:
                data = line.strip().split("|")
                if data[0] == book_id and data[3] == "Issued":
                    data[3] = "Available"
                    found = True
                updated.append("|".join(data))

        with open(self.file, "w") as f:
            for line in updated:
                f.write(line + "\n")

        if found:
            print("Book returned successfully!")
        else:
            print("Book not found or not issued.")

    def delete_book(self):
        book_id = input("Enter Book ID to delete: ")
        updated = []
        found = False

        with open(self.file, "r") as f:
            for line in f:
                data = line.strip().split("|")
                if data[0] != book_id:
                    updated.append(line)
                else:
                    found = True

        with open(self.file, "w") as f:
            f.writelines(updated)

        if found:
            print("Book deleted successfully!")
        else:
            print("Book not found.")


def main():
    lib = Library()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Delete Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            lib.add_book()
        elif choice == "2":
            lib.view_books()
        elif choice == "3":
            lib.issue_book()
        elif choice == "4":
            lib.return_book()
        elif choice == "5":
            lib.delete_book()
        elif choice == "6":
            print("Thank you for using Library System!")
            break
        else:
            print("Invalid choice!")


main()
