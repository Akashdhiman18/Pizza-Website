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
pizzas = [ 
    {'name':'True Italian Pizza', 'image': 'static/Neapolitan-Pizza.jpg.webp','ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce'},
    {'name':'Sicilian Pizza',  'image': 'static/Sicilian-Pizza.jpg.webp','ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce'}, 
    {'name':'Roman-style Pizza', 'image': 'static/Neapolitan-Pizza.jpg.webp','ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce'},
    {'name':'Staple American Pizza: ','image': 'static/Chicago-Deep-Dish-Pizza.jpg.webp', 'ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce'},
    {'name':'New York-style Pizza','image': 'static/New-York-Style-Pizza.jpg.webp', 'ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce'}, 
    {'name': 'Californian Pizza', 'image': 'static/Californian-Pizza.jpg.webp', 'ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce'}, 
    {'name': 'Detroit Pizza', 'image': 'static/Detroit-Pizza.jpg.webp', 'ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce'},
    {'name': 'St. Louis Pizza', 'image': 'static/St.-Louis-Pizza.jpg.webp' , 'ingredients':'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce'},
    {'name': 'Canadian Pizza', 'image': 'static/St.-Louis-Pizza.jpg.webp' , 'ingredients':'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce'},
    {'name': 'Mexican Pizza', 'image': 'static/Mexican-Pizza.jpg.webp', 'ingredients': 'Spiced paneer, Onion, Green Capsicum & Red Paprika in Tandoori Sauce'}, 
] 

pizza_sizes = [
    {'name': 'Small', 'price': 10},
    {'name': 'Medium', 'price': 15},
    {'name': 'Large', 'price': 20}, 
]

bases = [
{'name': 'Thin Crust', 'price': 2},
{'name': 'Thick Crust', 'price': 3},
{'name': 'Gluten-Free', 'price': 5},    
]

@app.route('/menu')
def menu():
    return render_template('menu.html', pizzas=pizzas)  

sides = [
    {'name':'Garlic Bread', 'image': 'static/Garlicbread.jpg','description': 'Buttery and garlicky, scattered with parsley, hot from  oven', 'price': 5.99},  
    {'name':'Onion Rings', 'image': 'static/Onion Rings.jpg','description': 'Sweetly and soft on  inside, with a crispy crunchy coating.', 'price': 5.99},
    {'name':'Fries', 'image': 'static/Fries.jpg.','description': 'Crunchy bites of fluffy potato, dip into aioli sauce for 50 cents more.', 'price': 5.99},  
    {'name':'Hash Bites', 'image': 'static/Hashbites.jpg','description': 'Crunchy bites of fluffy potato, dip into aioli sauce for 50 cents more.', 'price': 5.99}, 
    {'name':'Jalapeño Poppers', 'image': 'static/Jalapeno Poppers.jpg','description': '6 spicy poppers filled with cheese, corn and chopped Jalapeños.', 'price': 7.50},    
    {'name':'Chicken Bites', 'image': 'static/Chicken Bites.jpg','description': 'Southern style mini chicken bites with ranch sauce.', 'price': 7.50}, 
    {'name':'Bread Sticks', 'image': 'static/Breadsticks.jpg','description': 'Crispy on  outside, soft and chewy on  inside. Served with marinara dipping sauce. Try an order with cheese.', 'price': 6.50}, 
    {'name':'Cheesy Pull Apart Bread', 'image': 'static/Cheesy Bread.jpg','description': 'Warm baked dough bites coated in a buttery garlic glaze and covered in cheese.', 'price': 5.50}, 
    {'name':'Boneless Chicken Bites', 'image': 'static/Chicken Bites.jpg','description': 'Warm baked dough bites coated in a buttery garlic glaze and covered in cheese.', 'price': 8.50}, 
    {'name':'Caesar Salad', 'image': 'static/Caesar Salad.jpg','description':'Crisp romaine lettuce, croutons, and Caesar dressing.', 'price': 6.50},   
]

@app.route('/sides') 
def sides():
    return render_template('sides.html' , sides=sides)   

drinks = [ 
     {'name':'Coca Cola', 'image': 'static/Coca Cola.jpg'}, #Codes working but cant get the drink sizes up :<
     {'name':'Coke Zero', 'image': 'static/Coke Zero.jpg'}, 
     {'name':'Sprite', 'image': 'static/Sprite.jpg'},
     {'name':'Fanta', 'image': 'static/Fanta.jpg'},
     {'name':'L&P', 'image': 'static/L&P.jpg'},
     {'name':'Orange Juice', 'image': 'static/Orange Juice.jpg'},
     {'name':'Water', 'image': 'static/Water.jpg'},
]
drink_sizes = [
    {'name': '1.5L', 'price': 5.99}, 
    {'name': '600ml', 'price': 3.89},
    {'name': '330ml', 'price': 2.99},
]

@app.route('/drinks') 
def drinks():
    return render_template('drinks.html' , drinks=drinks)  

meal_deals = [  
    {'name': 'Double Value Deal', 'image': 'Double Value Deal.jpg', 'Description': '2 Large Pizzas & 2 Sides.' , 'price': 35.00},
    {'name': 'Triple Value Deal', 'image': 'Triple Value Deal.jpg', 'Description':'3 Large Pizzas & 2 Sides.' , 'price': 42.00},   
    {'name': 'Mega Value Deal', 'image': 'Mega Value Deal.jpg', 'Description': '4 Large Pizzas & 2 Sides.' , 'price': 49.00}, 
    {'name': 'Chicken Lovers Combo', 'image': 'Chicken Lovers Combo.jpg', 'Description': '1 large Chicken Pizza, Sourn Style Chicken Bites with Ranch Sauce and Garlic Bread.' , 'price': 29.00}, 
    {'name': '3 Pizza Deal', 'image': '3 Pizza Deal.jpg', 'Description':'3 Large Classic Value Pizzas.' , 'price': 33.00},  
    {'name': '3 Pizzas 3 Sides', 'image': '3 Pizzas 3 Sides.jpg', 'Description': '3 Large Classic Value Pizzas & 3 Sides. Sides include Garlic Bread, Fries or 1.5L Drink.' , 'price': 45.00},
    {'name': '4 Pizzas 4 Sides', 'image': '4 Pizzas 4 Sides.jpg', 'Description':'4 Large Classic Value Pizzas & 4 Sides. Sides include Garlic Bread, Fries or 1.5L Drink.' , 'price': 33.00},  
]

@app.route('/meal_deals') 
def meal_deals():
    return render_template('meal_deals.html', meal_deals=meal_deals)    

desserts = [
     {'name': 'Strawberry Cheesecake', 'image': 'static/Strawberry Cheesecake.jpg', 'Description': 'Velvety strawberry cheesecake on a sweet biscuit base.' , 'price': 6.39},
     {'name': 'Chocolate Lava Cake', 'image': 'static/Lava Cake.jpg', 'Description': 'Delicious Hershey’s chocolate cake with a warm, rich gooey centre, dusted with icing sugar' , 'price': 6.39},
     {'name': 'Chocolate Mousse', 'image': 'static/Chocolate Mousse.jpg', 'Description': 'A decadent, creamy swirl of chocolate mousse.' , 'price': 6.39}, 
     {'name': 'Strawberry Cheesecake', 'image': 'static/Strawberry Cheesecake.jpg', 'Description': 'Velvety strawberry cheesecake on a sweet biscuit base.' , 'price': 6.39},
     {'name': ' Ultimate Chocolate Chip Cookie', 'image': 'static/Chocolate Chip Cookie.jpg', 'Description': 'A giant chocolate chip cookie full of rich chocolate chips.' , 'price': 9.99},
     {'name': 'Cookie Dough Ice Cream', 'image': 'static/Cookie Dough Ice Cream.jpg'}, 
     #sizes for the ice cream  
]

@app.route('/desserts') 
def desserts():
    return render_template('desserts.html', desserts=desserts)   

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

