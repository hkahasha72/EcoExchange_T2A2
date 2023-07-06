from init import db, ma

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class CategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
        ordered = True
