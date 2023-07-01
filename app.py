from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://hope:recycleandtrade123@localhost:5432/eco'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

@app.cli.command('create')
def create_db():
    db.create_all()
    print('tables created successfully')

@app.route('/')
def index():
    return 'Hello, world'

if __name__ == '__main__':
    app.run(debug=True)
