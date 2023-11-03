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
    sides = [ 
        {
            'name': 'Garlic Bread',
            'image': 'static/Garlicbread.jpg',
            'description': 'Buttery and garlicky, scattered with parsley, hot from the oven.',
            'price': 6.99  
        }, 

        {
            'name': 'Onion Rings',
            'image': 'static/Onion Rings.jpg',
            'description': 'Sweetly and soft on the inside, with a crispy crunchy coating.',
            'price': 5.99   
        },

         {
            'name': 'Fries',
            'image': 'static/Fries.jpg',
            'description': 'Lightly golden, crinkle-cut and seasoned to perfection.',
            'price': 5.99 
             
        }, 

        {
        'name': 'Hash Bites',
        'image': 'static/Hashbites.jpg',
        'description': 'Crunchy bites of fluffy potato, dip into aioli sauce for 50 cents more.',
        'price': 5.99  
        }, 


        {
        'name': 'Jalapeño Poppers',
        'image': 'static/Jalapeno Poppers.jpg',
        'description': '6 spicy poppers filled with cheese, corn and chopped Jalapeños.',
        'price': 7.50  
        }, 

       {
        'name': 'Chickens Bites',
        'image': 'static/Chicken Bites.jpg',
        'description': 'Southern style mini chicken bites with ranch sauce.',
        'price': 6.50  # Add the price here
        },

        {
        'name': 'Bread Sticks',
        'image': 'static/Breadsticks.jpg',
        'description': 'Crispy on the outside, soft and chewy on the inside. Served with marinara dipping sauce. Try an order with cheese.',
        'price': 6.50  
        },

       {
        'name': 'Cheesy Pull Apart Bread',
        'image': 'static/Cheesy Bread.jpg',
        'description': 'Warm baked dough bites coated in a buttery garlic glaze and covered in cheese.',
        'price': 5.50
        },

        {
        'name': 'Boneless Chicken Bites',
        'image': 'static/Boneless Bites.jpg',
        'description': 'Warm baked dough bites coated in a buttery garlic glaze and covered in cheese.',
        'price': 8.50  
        },

        {
        'name': 'Caesar Salad',
        'image': 'static/Caesar Salad.jpg',
        'description': 'Crisp romaine lettuce, croutons, and Caesar dressing.',
        'price': 6.50
        },
    ] 

    return render_template('sides.html' , sides=sides) 

@app.route('/drinks')
def drinks():
    drinks= [
        {
            'name': 'Coca Cola',
            'image': 'static/Coca Cola.jpg',
            'sizes': [
                {'name': '1.5L', 'price': 5.99},
                {'name': '600ml', 'price': 3.89},
                {'name': '330ml', 'price': 2.99},
            ],
        },
         {
            'name': 'Coke Zero',
            'image': 'static/Coke Zero.jpg',  
            'sizes': [
                {'name': '1.5L', 'price': 5.99},
                {'name': '600ml', 'price': 3.89},
                {'name': '330ml', 'price': 2.99},
            ],  
            
        }, 

        {
            'name': 'Sprite', 
            'image': 'static/Sprite.jpg', 
            'sizes': [
                {'name': '1.5L', 'price': 5.99},
                {'name': '600ml', 'price': 3.89},
                {'name': '330ml', 'price': 2.99},
            ],  
            
        }, 

         {
            'name': 'Fanta', 
            'image': 'static/Fanta.jpg', 
            'sizes': [
                {'name': '1.5L', 'price': 5.99},
                {'name': '330ml', 'price': 2.99},
            ],  
            
        },

          {
            'name': 'L&P',
            'image': 'static/L&P.jpg', 
            'sizes': [
                {'name': '1.5L', 'price': 5.99},
            ],  
            
        }, 

        
       {
            'name': 'Orange Juice',
            'image': 'static/Orange Juice.jpg', 
            'sizes': [
                {'name': '330ml', 'price': 2.99},
            ],  
            
        },

        {
            'name': 'Water',
            'image': 'static/Water.jpg', 
            'sizes': [
                {'name': '1.5L', 'price': 5.99},
                {'name': '750ml', 'price': 3.99},  

            ],  
            
        },
    ]
    return render_template('drinks.html', drinks=drinks)  

@app.route('/meal_deals') 
def meal_deals():
    meal_deals= [
        {
            'name': 'Double Value Deal',
            'image': 'static/Double Value Deal.jpg',
            'description': 'B2 Large Pizzas & 2 Sides.',
            'price': 35.00  
        }, 

        {
            'name': 'Triple Value Deal',
            'image': 'static/Triple Value Deal.jpg',
            'description': '3 Large Pizzas & 2 Sides.',
            'price': 42.00 

        }, 

        {
            'name': 'Mega Value Deal',
            'image': 'static/Mega Value Deal.jpg',
            'description': '4 Large Pizzas & 2 Sides.',
            'price': 49.00              

        }, 

        {
            'name': 'Chicken Lovers Combo',
            'image': 'static/Chicken Lovers Combo.jpg',
            'description': '1 large Chicken Pizza, Southern Style Chicken Bites with Ranch Sauce and Garlic Bread.', 
            'price': 29.00 

        },

        {
            'name': '3 Pizza Deal',
            'image': 'static/3 Pizza Deal.jpg',
            'description': '3 Large Classic Value Pizzas.',
            'price': 33.00

        }, 

         {
            'name': '3 Pizzas 3 Sides',
            'image': 'static/3 Pizza 3 Sides.jpg', 
            'description': '3 Large Classic Value Pizzas & 3 Sides. Sides include Garlic Bread, Fries or 1.5L Drink.', 
            'price': 45.00 

        }, 

         {
            'name': '4 Pizzas 4 Sides',
            'image': 'static/4 Pizza 4 Sides.jpg', 
            'description': '4 Large Classic Value Pizzas & 4 Sides. Sides include Garlic Bread, Fries or 1.5L Drink.', 
            'price': 56.00 

        },  

    ]
    return render_template('meal_deals.html') 

@app.route('/desserts')
def desserts():
    return render_template('desserts.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/store_location')
def store_location():
    return render_template('store_location.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')


if __name__ == '__main__':
    app.run(debug=True)

 