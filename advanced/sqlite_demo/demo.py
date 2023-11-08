# import sqlite3
#
# db = sqlite3.connect('months-collection.db')
#
# cursor = db.cursor()
#
# # cursor.execute('CREATE TABLE books'
# #                '(id INTEGER PRIMARY KEY,'
# #                'title varchar(250) NOT NULL UNIQUE,'
# #                'author varchar (250) NOT NULL,'
# #                'rating FLOAT NOT NULL)'
# #                )
#
# cursor.execute("INSERT INTO books VALUES (1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.sqlite3'

db = SQLAlchemy()
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


with app.app_context():
    db.create_all()

# #Create Record
# with app.app_context():
#     new_book = Books(title='Veskos adventures', author='J. K. Rowling', rating=3.2)
#     db.session.add(new_book)
#     db.session.commit()

#Read All Records
# with app.app_context():
#     result = db.session.execute(db.select(Books).order_by(Books.title))
#     all_books = result.scalars()
#     for book in all_books:
#        print(book.__repr__())

# Read a Particular Record By Query
# with app.app_context():
#     book = db.session.execute(db.select(Books).where(Books.title == 'Spas')).scalar()
#     print(book.__repr__())

# Update A Particular Record By Query
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()
#

# Update a Record By Primary Key
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id)
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()

# Delete a Particular Record By Primary Key
# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
