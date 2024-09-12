# category.py

from flask import abort, make_response

from config import db
from models import Category, categories_schema

def list_category():
    category = Category.query.all()
    return categories_schema.dump(category)