from init import db, ma
from marshmallow import fields
from datetime import datetime

class PersonalMessage(db.Model):
    __tablename__ = 'personal_messages'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  # Added date_created column

class PersonalMessageSchema(ma.Schema):
    sender = fields.Nested('UserSchema', only=['name', 'email'])
    receiver = fields.Nested('UserSchema', only=['name', 'email'])

    class Meta:
        fields = ('id', 'sender_id', 'receiver_id', 'message', 'sender', 'receiver', 'date_created')  # Added date_created field
        ordered = True