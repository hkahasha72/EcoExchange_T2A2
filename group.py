from init import db, ma
from marshmallow import fields
from datetime import datetime

class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    members = db.relationship('User', secondary='user_group', backref='groups')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  
    
    # Added date_created column

class GroupSchema(ma.Schema):
    members = fields.Nested('UserSchema', many=True, only=['id', 'name', 'email'])

    class Meta:
        fields = ('id', 'name', 'members', 'date_created')  # Added date_created field
        ordered = True