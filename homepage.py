from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_cart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pizza_name = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(20), nullable=False)
    base = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)


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
            'name': ' True Italian Pizza ',
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
            'name': ' Sicilian Pizza',
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
            'name': 'Staple American Pizza: ',
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
            'name': ' New York-style Pizza',
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
            'name': ' Californian Pizza',
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
            'name': ' Detroit Pizza',
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
            'name': ' St. Louis Pizza',
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
            'name': ' Mexican Pizza',
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
            'description': 'Buttery and garlicky, scattered with parsley, hot from  oven.',
            'price': 6.99  
        }, 

        {
            'name': 'Onion Rings',
            'image': 'static/Onion Rings.jpg',
            'description': 'Sweetly and soft on  inside, with a crispy crunchy coating.',
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
        'description': 'Sourn style mini chicken bites with ranch sauce.',
        'price': 6.50  # Add  price here
        },

        {
        'name': 'Bread Sticks',
        'image': 'static/Breadsticks.jpg',
        'description': 'Crispy on  outside, soft and chewy on  inside. Served with marinara dipping sauce. Try an order with cheese.',
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
            'description': '1 large Chicken Pizza, Sourn Style Chicken Bites with Ranch Sauce and Garlic Bread.', 
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
    return render_template('meal_deals.html' , meal_deals=meal_deals)  

@app.route('/desserts')
def desserts():
    desserts= [

         {
            'name': 'Strawberry Cheesecake',
            'image': 'static/Strawberry Cheesecake.jpg',
            'description': 'Velvety strawberry cheesecake on a sweet biscuit base.',
            'price': 6.39 
        }, 

         {
            'name': 'Chocolate Lava Cake',
            'image': 'static/Lava Cake.jpg',
            'description': 'Delicious Hershey’s chocolate cake with a warm, rich gooey centre, dusted with icing sugar', 
            'price': 6.39 
        }, 

           {
            'name': 'Chocolate Mousse',
            'image': 'static/Chocolate Mousse.jpg',
            'description': 'A decadent, creamy swirl of chocolate mousse.',  
            'price': 6.39 
        }, 

           {
            'name': ' Ultimate Chocolate Chip Cookie',
            'image': 'static/Chocolate Chip Cookie.jpg',
            'description': 'A giant chocolate chip cookie full of rich chocolate chips.',  
            'price': 9.99
        }, 

          {
            'name': 'Cookie Dough Ice Cream', 
            'image': 'static/Cookie Dough Ice Cream.jpg', 
            'sizes': [
                {'name': '1 Pint', 'price': 16.49},
                {'name': '4 Ounces', 'price': 7.49},
                
            ],  
            
        }, 

    ]
    return render_template('desserts.html' , desserts=desserts) 

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

 