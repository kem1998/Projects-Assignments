from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Float, Date, ForeignKey
from sqlalchemy.orm import relationship 
from dateutil.parser import parse

Base = declarative_base()

class Borrower(Base): 

    __tablename__ = 'borrower'

    borrower_id = Column(Integer, primary_key=True) 
    first_name = Column(String(255), nullable=False) 
    last_name = Column(String(255), nullable=False) 
    date_of_birth = Column(String(255), nullable=False) 
    email_address = Column(String(255), nullable=False, unique=True) 
    mobile_number = Column(String(20), nullable=False, unique=True) 
    street_address = Column(String(255),nullable=False) 
    suburb = Column(String(255),nullable=False) 
    state = Column(String(3),nullable=False) 
    postcode = Column(String(5),nullable=False) 


class Book(Base): 

    __tablename__ = 'book'

    isbn = Column(Integer, primary_key=True) 
    title = Column(String(255), nullable=False) 
    publisher = Column(String(255), nullable=False) 
    author = Column(String(255), nullable=False) 
    date_published = Column(String(255), nullable=False, unique=True) 
    location = Column(String(20), nullable=False, unique=True) 


class Librarian(Base): 

    __tablename__ = 'librarian'

    librarian_id = Column(Integer, primary_key=True) 
    first_name = Column(String(255), nullable=False) 
    last_name = Column(String(255), nullable=False)
    email_address = Column(String(255), nullable=False, unique=True) 
    mobile_number = Column(String(20), nullable=False, unique=True)   


class Loan(Base): 

    __tablename__ = 'loan'

    loan_id = Column(Integer, primary_key=True)   
    borrower_id = Column(Integer, ForeignKey("borrower.borrower_id"))
    isbn = Column(Integer, ForeignKey("book.isbn"))
    librarian_id = Column(Integer, ForeignKey("librarian.librarian_id"))