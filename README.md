# Library Management System

A simple Library Management System built with Python and SQLAlchemy. This program allows you to manage members, books, and transactions through a command-line interface.

## Features

- Add and list library members
- Add and list books
- Borrow and return books
- Track transactions

## Getting Started

### Prerequisites

- Python 3.10.12 version
- SQLAlchemy

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd library-management

2. Install the required packages:

    pip install sqlalchemy

3.Set up the database and seed it with initial data:
  
    python lib/models.py

## Running the CLI

 To start the command-line interface, run:

   python lib/cli.py

Available Commands:
 0: Exit the program
1: List all members
2: Add a new member
3: List all books
4: Add a new book
5: List all transactions
6: Borrow a book
7: Return a book

## Database Models

  The system uses the following models:

1.Member: Represents library members with id, name, and email.

2.Book: Represents books with id, title, and author.

3.Transaction: Represents borrowing/returning books, linking member_id and book_id.

## Configuration

  Database configuration is handled in lib/config.py. By default, it uses SQLite, but you can modify the DATABASE_URL to use other databases like PostgreSQL or MySQL.

## Contributing

  Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and improvements.

## licence

 This project is licensed under the MIT License. See the LICENSE file for more details.

 ## Author 
   
   Daniel Kipkurui Bundotich
