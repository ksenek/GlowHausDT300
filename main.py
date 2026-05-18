from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "glosshaus.db"

def create_connection(db_file):
  """create connection to database"""
  try:
    connection = sqlite3.connect(db_file)
    return connection
  except Error as e:
    print(e)
  return None

@app.route('/')
def render_homepage():
  return render_template('home.html')


@app.route('/products')
def render_products_page():
  con = create_connection(DATABASE)
  query = "SELECT name, description, size, image, price FROM products"
  cur = con.cursor()
  cur.execute(query)
  product_list = cur.fetchall()
  con.close()

  return render_template('products.html', products=product_list)


@app.route('/contact')
def render_contact_page():
  return render_template('contact.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)