from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.book import Book, BookList
from resources.library import Library, LibraryList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'amy'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Book, '/book/<string:title>')
api.add_resource(BookList, '/books')
api.add_resource(UserRegister, '/register')
api.add_resource(Library, '/library/<string:name>')
api.add_resource(LibraryList, '/libraries')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
