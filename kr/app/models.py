
from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer)
    name = db.Column(db.String(64), unique=True)
    instock = db.Column(db.Boolean, default=False)
    number = db.Column(db.Integer)
    cost = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(140))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return f'{self.uname}, {self.category}'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64))
    product = db.relationship('Product', backref='category', lazy='dynamic')
    
    
    def __repr__(self):
        return f'{self.category}'
