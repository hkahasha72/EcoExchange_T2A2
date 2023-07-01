from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://hope:recycleandtrade123@localhost:5432/eco'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String)

# Create schema classes for serialization/deserialization
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'is_admin')

class ItemPost(db.Model):
    __tablename__ = 'item_posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref('item_posts', lazy=True))

# Create schema classes for serialization/deserialization
class ItemPostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'price', 'user_id')

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
                email='mahif@gmail.com',
                password='mahik'
            ),
            User(
                name='Kahasha',
                email='kahasha@gmail.com',
                password='kahashak'
            ),
        ]

        # Truncate the User table
        db.session.query(User).delete()

        # Add the User objects to the session
        db.session.add_all(Users)

        # Create some ItemPosts
        item_posts = [
            ItemPost(
                title='Couch',
                description='Couch was bought 7 months ago, im moving so i wanted to exchange it for moving equipment',
                price=100,
                user=Users[0]
            ),
            ItemPost(
                title='Spare wood',
                description='have some spare wood from my pallet due to big warehouse delivery, dont wanna leave it lying around, willing to exchange all 7 pallets for help unloading',
                price=0,
                user=Users[1]
            ),
            ItemPost(
                title='Cans',
                description='Had a party and have 12 crates of empty cans worth 10c each can, willing to give away for free, have an inspection in 2 days and bins dont come until the following week and dont have car to go drop it off',
                price=0,
                user=Users[2]
            )
        ]
        db.session.query(ItemPost).delete()
        db.session.add_all(item_posts)

        # Commit the transaction to the database
        db.session.commit()
        print('Models seeded')

@app.route('/users')
def all_users():
    users = User.query.order_by(User.name).all()
    return UserSchema(many=True).dumps(users)

@app.route('/item_posts')
def all_item_posts():
    item_posts = ItemPost.query.all()
    return ItemPostSchema(many=True).dumps(item_posts)

@app.route('/')
def index():
    return 'Hello, world'

if __name__ == '__main__':
    app.run(debug=True)
