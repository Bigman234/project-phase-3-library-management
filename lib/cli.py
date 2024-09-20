from library import (
    list_members,
    add_member,
    list_books,
    add_book,
    list_transactions,
    borrow_book,
    return_book,
)
from database import session  # Assuming you have a db.py file for session management

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_members()
        elif choice == "2":
            add_member()
        elif choice == "3":
            list_books()
        elif choice == "4":
            add_book()
        elif choice == "5":
            list_transactions()
        elif choice == "6":
            borrow_book()
        elif choice == "7":
            return_book()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all members")
    print("2. Add a new member")
    print("3. List all books")
    print("4. Add a new book")
    print("5. List all transactions")
    print("6. Borrow a book")
    print("7. Return a book")

def exit_program():
    print("Exiting the program...")
    session.close()  # Close the database session if applicable
    exit(0)
    
if __name__ == "__main__":
    main()
    