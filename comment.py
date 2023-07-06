from init import db, ma
from marshmallow import fields
from datetime import datetime

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    item_post_id = db.Column(db.Integer, db.ForeignKey('item_posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='comments')
    item_post_id = db.Column(db.Integer, db.ForeignKey('item_posts.id'))
    item_post = db.relationship('ItemPost', back_populates='comments')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  # Added date_created column

class CommentSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    item_post = fields.Nested('ItemPostSchema', only=['title', 'description', 'price'])

    class Meta:
        fields = ('id', 'text', 'date_created', 'user', 'item_post')  # Added date_created field
        ordered = True
