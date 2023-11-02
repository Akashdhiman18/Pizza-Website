from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_cart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(20), nullable=False)
    base = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

image_lookup = {
    'small': {
        'thin': 'static/small_thin.jpg',
        'thick': 'static/small_thick.jpg',
        'Gluten-Free': 'static/small_gluten_free.jpg'
    },
    'Medium': {
        'thin': 'static/medium_thin.jpg',
        'thick': 'static/medium_thick.jpg',
        'Gluten-Free': 'static/medium_gluten_free.jpg'
    },
    'Large': {
        'thin': 'static/large_thin.jpg',
        'thick': 'static/large_thick.jpg',
        'Gluten-Free': 'static/large_gluten_free.jpg'
    }
}

@app.route('/remove/<int:item_id>')
def remove_item(item_id):
    item = CartItem.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return redirect('/menu')

@app.route('/')
def home():
    return render_template('index.html')
    


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/menu')
def menu():
    pizzas = [
        {
            'name': 'The True Italian Pizza: Neapolitan ',
            'image': 'static/Neapolitan-Pizza.jpg.webp',
            'ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce',
            'sizes': [
                {'name': 'Small', 'price': 10},
                {'name': 'Medium', 'price': 15},
                {'name': 'Large', 'price': 20}
            ],
            'bases': [
                {'name': 'Thin Crust', 'price': 2},
                {'name': 'Thick Crust', 'price': 3},
                {'name': 'Gluten-Free', 'price': 5}
            ]
        },
        {
            'name': 'The Sicilian Pizza',
            'image': 'static/Sicilian-Pizza.jpg.webp',
            'ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce',
            'sizes': [
                {'name': 'Small', 'price': 10},
                {'name': 'Medium', 'price': 15},
                {'name': 'Large', 'price': 20}
            ],
            'bases': [
                {'name': 'Thin Crust', 'price': 2},
                {'name': 'Thick Crust', 'price': 3},
                {'name': 'Gluten-Free', 'price': 5}
            ]
        },
        {
            'name': 'Roman-style Pizza',
            'image': 'static/Roman-Style-Pizza.jpg.webp',
            'ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce',
            'sizes': [
                {'name': 'Small', 'price': 10},
                {'name': 'Medium', 'price': 15},
                {'name': 'Large', 'price': 20}
            ],
            'bases': [
                {'name': 'Thin Crust', 'price': 2},
                {'name': 'Thick Crust', 'price': 3},
                {'name': 'Gluten-Free', 'price': 5}
            ]
        },
        {
            'name': 'The Staple American Pizza: Chicago Deep-dish, New York- or Detroit-Style Pizza',
            'image': 'static/Chicago-Deep-Dish-Pizza.jpg.webp',
            'ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce',
            'sizes': [
                {'name': 'Small', 'price': 10},
                {'name': 'Medium', 'price': 15},
                {'name': 'Large', 'price': 20}
            ],
            'bases': [
                {'name': 'Thin Crust', 'price': 2},
                {'name': 'Thick Crust', 'price': 3},
                {'name': 'Gluten-Free', 'price': 5}
            ]
        },
        {
            'name': 'The New York-style Pizza',
            'image': 'static/New-York-Style-Pizza.jpg.webp',
            'ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce',
            'sizes': [
                {'name': 'Small', 'price': 10},
                {'name': 'Medium', 'price': 15},
                {'name': 'Large', 'price': 20}
            ],
            'bases': [
                {'name': 'Thin Crust', 'price': 2},
                {'name': 'Thick Crust', 'price': 3},
                {'name': 'Gluten-Free', 'price': 5}
            ]
        },
        {
            'name': 'The Californian Pizza',
            'image': 'static/Californian-Pizza.jpg.webp',
            'ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce',
            'sizes': [
                {'name': 'Small', 'price': 10},
                {'name': 'Medium', 'price': 15},
                {'name': 'Large', 'price': 20}
            ],
            'bases': [
                {'name': 'Thin Crust', 'price': 2},
                {'name': 'Thick Crust', 'price': 3},
                {'name': 'Gluten-Free', 'price': 5}
            ]
        },
        {
            'name': 'The Detroit Pizza',
            'image': 'static/Detroit-Pizza.jpg.webp',
            'ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce',
            'sizes': [
                {'name': 'Small', 'price': 10},
                {'name': 'Medium', 'price': 15},
                {'name': 'Large', 'price': 20}
            ],
            'bases': [
                {'name': 'Thin Crust', 'price': 2},
                {'name': 'Thick Crust', 'price': 3},
                {'name': 'Gluten-Free', 'price': 5}
            ]
        },
        {
            'name': 'The St. Louis Pizza',
            'image': 'static/St.-Louis-Pizza.jpg.webp',
            'ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce',
            'sizes': [
                {'name': 'Small', 'price': 10},
                {'name': 'Medium', 'price': 15},
                {'name': 'Large', 'price': 20}
            ],
            'bases': [
                {'name': 'Thin Crust', 'price': 2},
                {'name': 'Thick Crust', 'price': 3},
                {'name': 'Gluten-Free', 'price': 5}
            ]
        },
        {
            'name': 'Canadian Pizza',
            'image': 'static/Nova-Scotia-Garlic-Fingers-Pizza.jpg.webp',
            'ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce',
            'sizes': [
                {'name': 'Small', 'price': 10},
                {'name': 'Medium', 'price': 15},
                {'name': 'Large', 'price': 20}
            ],
            'bases': [
                {'name': 'Thin Crust', 'price': 2},
                {'name': 'Thick Crust', 'price': 3},
                {'name': 'Gluten-Free', 'price': 5}
            ]
        },
        {
            'name': 'The Mexican Pizza',
            'image': 'static/Mexican-Pizza.jpg.webp',
            'ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce',
            'sizes': [
                {'name': 'Small', 'price': 10},
                {'name': 'Medium', 'price': 15},
                {'name': 'Large', 'price': 20}
            ],
            'bases': [
                {'name': 'Thin Crust', 'price': 2},
                {'name': 'Thick Crust', 'price': 3},
                {'name': 'Gluten-Free', 'price': 5}
            ]
        },
        
    ]
    return render_template('menu.html', pizzas=pizzas)


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








if __name__ == '__main__':
    app.run(debug=True)

 