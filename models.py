# models.py

from marshmallow_sqlalchemy import fields

from config import db, ma


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String)

class CategorySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Category
        load_instance = True
        sqla_session = db.session
        include_relationships = True


categories_schema = CategorySchema(many=True)
