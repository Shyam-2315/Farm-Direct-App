from config import app, db
from models import Category

CATEGORIES = [
    {
        "name": "Aata, Rice & Dal",
        "image": "../static/images/category/category-atta-rice-dal.jpg",
    },
    {
        "name": "Pet Care",
        "image": "../static/images/category/category-pet-care.jpg",
    },
    {
        "name": "Bakery & Biscuits",
        "image": "../static/images/category/category-bakery-biscuits.jpg",
    },
    {
        "name": "Vgetables",
        "image": "../static/images/category/category-vegetables.jpg",
    },
    {
        "name": "Vegetables Oil",
        "image": "../static/images/category/category-vegetable-oil.jpg",
    },
    {
        "name": "Cereals",
        "image": "../static/images/category/category-cereal.jpg",
    },
    {
        "name": "Dairy, Bread & Eggs",
        "image": "../static/images/category/category-dairy-bread-eggs.jpg",
    },
    {
        "name": "Instant Food",
        "image": "../static/images/category/category-instant-food.jpg",
    },
    {
        "name": "Snack & Munchies",
        "image": "../static/images/category/category-snack-munchies.jpg",
    },
    {
        "name": "Tea, Coffee & Drinks",
        "image": "../static/images/category/category-tea-coffee-drinks.jpg",
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in CATEGORIES:
        new_category = Category(name=data.get("name"), image=data.get("image"))
        db.session.add(new_category)
    db.session.commit()
