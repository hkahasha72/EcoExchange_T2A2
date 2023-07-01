from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://hope:recycleandtrade123@localhost:5432'

db = SQLAlchemy(app)
print(db.__dict__)

@app.route('/')
def index():
    return 'Hello, world'

if __name__ == '__main__':
    app.run(debug=True)
