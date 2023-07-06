from flask import Blueprint
from init import db, bcrypt, app
from models.usergroup import UserGroup
from models.user import User
from models.itempost import ItemPost
from models.comment import Comment
from models.personalmessage import PersonalMessage
from models.group import Group
from models.category import Category

cli_bp = Blueprint('db', __name__)

@cli_bp.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all()
    print("Tables have been created successfully")

@cli_bp.cli.command('seed')
def seed_db():
    db.session.query(UserGroup).delete()
    db.session.query(Group).delete()
   

    # Add the User objects to the session
    Users = [
        User(
            name='Hope',
            email='hope@gmail.com',
            password=bcrypt.generate_password_hash('hopek').decode('utf-8'),
            is_admin=True
        ),
        User(
            name='Mahi',
            email='mahif@gmail.com',
            password=bcrypt.generate_password_hash('mahik').decode('utf-8'),
        ),
        User(
            name='Kahasha',
            email='kahasha@gmail.com',
            password=bcrypt.generate_password_hash('kahashak').decode('utf-8'),
        ),
    ]
    db.session.query(User).delete()
    db.session.add_all(Users)
    db.session.commit()

    Categories = [
        Category(
            name='Furniture'
        ),
        Category(
            name='Electronics'
        ),
        Category(
            name='Reusable Materials'
        ),
    ]
    db.session.query(Category).delete()
    db.session.add_all(Categories)
    db.session.commit()

    # Create some ItemPosts
    item_posts = [
        ItemPost(
            title='Couch',
            description='Couch was bought 7 months ago, I am moving so I wanted to exchange it for moving equipment',
            price=100,
            user=Users[0],
            category=Categories[0]
        ),
        ItemPost(
            title='Spare wood',
            description='Have some spare wood from my pallet due to a big warehouse delivery. I don\'t wanna leave it lying around. Willing to exchange all 7 pallets for help unloading.',
            price=0,
            user=Users[1],
            category=Categories[0]
        ),
        ItemPost(
            title='Cans',
            description='Had a party and have 12 crates of empty cans worth 10 cents each can. Willing to give away for free. Have an inspection in 2 days and bins don\'t come until the following week and I don\'t have a car to go drop it off.',
            price=0,
            user=Users[2],
            category=Categories[2]
        )
    ]
    db.session.query(ItemPost).delete()
    db.session.add_all(item_posts)
    db.session.commit()

    # Create some Comments
    comments = [
        Comment(
            text='This couch looks great! Is it still available?',
            item_post=item_posts[0]
        ),
        Comment(
            text='I can help you unload the wood. Let me know when and where.',
            item_post=item_posts[1]
        ),
        Comment(
            text='I\'m interested in the cans. Can I come pick them up tomorrow?',
            item_post=item_posts[2]
        ),
    ]
    db.session.query(Comment).delete()
    db.session.add_all(comments)
    db.session.commit()

    # Create some PersonalMessages
    personal_messages = [
            PersonalMessage(
                sender=Users[0],
                receiver=Users[1],
                message='Hey, are you still interested in the couch?'
            ),
            PersonalMessage(
                sender=Users[1],
                receiver=Users[0],
                message='Yes, I am. Can we arrange a time for pickup?'
            ),
    ]
    db.session.query(PersonalMessage).delete()
    db.session.add_all(personal_messages)
    db.session.commit()

    groups = [
        Group(
            name='VIC suburbs',
            members=Users[0],
            date_created='2023-07-02'
        ),
        Group(
            name='SA suburbs',
            members=Users[1],
            date_created='2023-07-02'
        ),
        Group(
            name='WA suburbs',
            members=Users[2],
            date_created='2023-07-02'
        ),
    ]
    db.session.query(Group).delete()
    db.session.add_all(groups)
    db.session.commit()

    print('Tables seeded')
