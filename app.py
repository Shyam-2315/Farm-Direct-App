# app.py

from flask import render_template
import config
from models import Category

app = config.connex_app

@app.route("/")
def home():
  category = Category.query.all()
  return render_template('home.html', category=category,  name='FarmDirect')


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)
