from init import db, ma
from marshmallow import fields
from datetime import datetime

class ItemPost(db.Model):
    __tablename__ = 'item_posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='item_post', lazy=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category', backref='item_posts', lazy=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow) 

class ItemPostSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    comments = fields.Nested('CommentSchema', many=True, only=['id', 'text'])
    category = fields.Nested('CategorySchema', only=['id', 'name'])

    class Meta:
        fields = ('id', 'title', 'description', 'price', 'user', 'comments', 'category', 'date_created')  # Added date_created field
        ordered = True
