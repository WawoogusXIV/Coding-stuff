from flask import Flask
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.name} - {self.author}"


@app.route('/')
def index():
    return("<h1>Hi!</h1>")

@app.route('/Books')
def get_books():
    books = Book.query.all()

    output = []

    for book in books:
        book_data = {"name": book.name, "author":book.author, "publisher": book.publisher}
        output.append(book_data)
    return {"books": output}

@app.route('/Books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return{"name": book.name, "author": book.author, "publisher": book.publisher}

@app.route('/Books', methods=['POST'])
def add_drink():
    book = Book(name=request.json['name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()

    return {'id:': book.id}

@app.route('/Books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"Error": "Not Found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "Byeeee <3"}