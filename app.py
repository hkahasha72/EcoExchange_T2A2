from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://hope:recycleandtrade123@localhost:5432/eco'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

# Create schema classes for serialization/deserialization
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password')
        

@app.cli.command('create')
def create_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        print('Tables created successfully')

@app.cli.command('seed')
def seed_db():
    with app.app_context():
      Users = [
        User(
            name='Hope',
            email='hope@gmail.com',
            password='hopek'
        ),
        User(
            name='Mahi',
            email='hope@gmail.com',
            password='hopek'
        ),
        User(
            name='kahasha',
            email='hope@gmail.com',
            password='hopek'
        ),
        ]

    # Truncate the User table
    db.session.query(User).delete()

    # Add the User object to the session
    db.session.add_all(Users)

    # Commit the transaction to the database
    db.session.commit()
    print('Models seeded')

@app.route('/users')
def all_users():
    # select * from "users"
    stmt = db.select(User).order_by(User.name)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True).dumps(users)


@app.route('/')
def index():
    return 'Hello, world'

if __name__ == '__main__':
    app.run(debug=True)

