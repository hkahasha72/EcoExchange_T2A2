from init import db, ma
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)
    item_posts = db.relationship('ItemPost', backref='user', lazy=True)
    personal_messages_sent = db.relationship('PersonalMessage', backref='sender', lazy=True, foreign_keys='PersonalMessage.sender_id')
    personal_messages_received = db.relationship('PersonalMessage', backref='receiver', lazy=True, foreign_keys='PersonalMessage.receiver_id')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  # Added date_created column

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'is_admin', 'date_created')  # Added date_created field
        ordered = True
