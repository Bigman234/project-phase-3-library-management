from sqlalchemy.orm import sessionmaker
from models import Member, Book, Transaction, Base
from config import engine

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Recreate database tables
Base.metadata.drop_all(bind=engine)  # Optional: Drops all tables before creating them again
Base.metadata.create_all(bind=engine)

# Seed Data
def seed_data():
    # Create Members
    member1 = Member(name="Alice")
    member2 = Member(name="Bob")
    member3 = Member(name="Charlie")
    
    session.add_all([member1, member2, member3])
    session.commit()

    # Create Books
    book1 = Book(title="1984", author="George Orwell")
    book2 = Book(title="To Kill a Mockingbird", author="Harper Lee")
    book3 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald")
    
    session.add_all([book1, book2, book3])
    session.commit()

    # Create Transactions (e.g., borrowing books)
    transaction1 = Transaction(member_id=member1.id, book_id=book1.id)
    transaction2 = Transaction(member_id=member2.id, book_id=book2.id)
    
    session.add_all([transaction1, transaction2])
    session.commit()

    print("Seed data added successfully!")
if __name__ == "__main__":
    seed_data()