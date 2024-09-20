from database import session
from models import Member, Book, Transaction
from sqlalchemy.exc import IntegrityError

def list_members():
    members = session.query(Member).all()
    for member in members:
        print(f"ID: {member.id}, Name: {member.name}, Email: {member.email}")

def add_member():
    name = input("Enter member name: ")
    email = input("Enter member email: ")  # Collect the email
    new_member = Member(name=name, email=email)  # Include email when creating the member
    session.add(new_member)
    try:
        session.commit()
        print(f"Member '{name}' added successfully.")
    except IntegrityError as e:
        print("Error adding member:", e)
        session.rollback()  # Roll back the session in case of error

def list_books():
    books = session.query(Book).all()
    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}")

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    new_book = Book(title=title, author=author)
    session.add(new_book)
    try:
        session.commit()
        print(f"Book '{title}' by {author} added successfully.")
    except IntegrityError as e:
        print("Error adding book:", e)
        session.rollback()  # Roll back the session in case of error

def list_transactions():
    transactions = session.query(Transaction).all()
    for transaction in transactions:
        print(f"Transaction ID: {transaction.id}, Member ID: {transaction.member_id}, Book ID: {transaction.book_id}, Status: {'Returned' if transaction.returned else 'Borrowed'}")

def borrow_book():
    member_id = int(input("Enter member ID: "))
    book_id = int(input("Enter book ID: "))
    new_transaction = Transaction(member_id=member_id, book_id=book_id)
    session.add(new_transaction)
    try:
        session.commit()
        print(f"Book with ID {book_id} borrowed by member ID {member_id}.")
    except IntegrityError as e:
        print("Error processing transaction:", e)
        session.rollback()  # Roll back the session in case of error

def return_book():
    transaction_id = int(input("Enter transaction ID: "))
    transaction = session.query(Transaction).get(transaction_id)
    if transaction:
        transaction.returned = True
        session.commit()
        print(f"Book returned for transaction ID {transaction_id}.")
    else:
        print("Transaction not found.")

