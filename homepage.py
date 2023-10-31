from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def menu():
    return render_template('menu.html') 

@app.route('/sides')
def sides():
    return render_template('sides.html') 

@app.route('/drinks')
def drinks():
    return render_template('drinks.html')

@app.route('/meal_deals')
def meal_deals():
    return render_template('meal_deals.html') 

@app.route('/desserts')
def desserts():
    return render_template('desserts.html')

@app.route('/store_location')
def store_location():
    return render_template('store_location.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

# Database initialization and connection
conn = sqlite3.connect('pizza_cart.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS cart_items
               (id INTEGER PRIMARY KEY AUTOINCREMENT, size TEXT, base TEXT, price REAL)''')
conn.commit()

@app.route('/cart')
def cart():
    # Retrieve cart items from the database
    cur.execute('SELECT * FROM cart_items')
    cart_items = cur.fetchall()

    # Calculate total price
    total_price = sum(item[3] for item in cart_items)

    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    size = data['size']
    base = data['base']
    price = data['price']

    # Insert the selected item into the database
    cur.execute('INSERT INTO cart_items (size, base, price) VALUES (?, ?, ?)', (size, base, price))
    conn.commit()

    return jsonify({'message': 'Item added to cart successfully'})

    


 

if __name__ == '__main__':
    app.run(debug=True) 
 