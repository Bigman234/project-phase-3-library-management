from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config import Base

class Member(Base):
    __tablename__ = 'members'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Member(name={self.name}, email={self.email})>"
    
class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author})>"

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    borrowed_date = Column(DateTime)
    return_date = Column(DateTime)
  

    member = relationship("Member", back_populates="transactions")
    book = relationship("Book", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(member_id={self.member_id}, book_id={self.book_id})>"

Member.transactions = relationship("Transaction", order_by=Transaction.id, back_populates="member")
Book.transactions = relationship("Transaction", order_by=Transaction.id, back_populates="book")    