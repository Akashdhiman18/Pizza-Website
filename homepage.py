from flask import Flask, render_template, request, redirect, url_for, session, jsonify,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_cart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'QWERTYUIOP'
db = SQLAlchemy(app)

# Initialize a list to store cart items (temporary storage)
cart_items = []

class Dessert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    # Add other relevant fields

class MealDeal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    # Add other relevant fields

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    # Add other relevant fields

# Define a CartItem class to represent items in the shopping cart
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    size = db.Column(db.String(50))
    base = db.Column(db.String(50))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer) 

# Define a UserSignIn class to represent user information for authentication
class UserSignIn(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
#     payments = relationship('Payment', backref='user', lazy=True)
#     order_details = relationship('OrderDetail', backref='user', lazy=True)

# #defined a Payment class to represent 


# class Payment(db.Model):
#     payment_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user_sign_in.user_id'))
#     amount = db.Column(db.Float)
#     date = db.Column(db.Date)  
#     time = db.Column(db.Time) 
#     order_id = db.Column(db.Integer, db.ForeignKey('order_detail.order_id'))  


# class OrderDetail(db.Model):
#     order_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user_sign_in.user_id'))
#     item_name = db.Column(db.String(255))
#     quantity = db.Column(db.Integer)
#     date = db.Column(db.Date) 
#     time = db.Column(db.Time)  
#     address = db.Column(db.String(255))  
#     phone_number = db.Column(db.String(20)) 
#     payments = relationship('Payment', backref='order_detail', lazy=True)





















@app.route('/process_form', methods=['POST'])
def process_form():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        
        try:
            user = UserSignIn(name=name, password=password, email=email)
            db.session.add(user)
            db.session.commit()
            flash("You are successfully registered. Now you can order your favorite food.", 'success')
            return redirect(url_for('home'))
        except Exception as e:
            print("Error:", str(e))
            db.session.rollback()
            flash("Error occurred during registration. Please try again.", 'error')
    
    return render_template('index.html')

#use login section ------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    # Handle login form submission
    if request.method == 'POST':
        global user_authenticated
        email = request.form['email']
        password = request.form['password']

        # Check if the email and password are correct by querying the database
        user = UserSignIn.query.filter_by(email=email, password=password).first()
        if user:
            # If the user is found, log them in and set session variables
            user_authenticated = True
            session['user_id'] = user.userid
            session['user_name'] = user.name
            session['user_email'] = user.email
            return redirect('menu')
        else:
            # If the user is not found, display an error message
            return render_template('index.html', error_message='Invalid email or password.')
    else:
        # If the request is a GET request, display the login form
        return render_template('index.html', user_authenticated=user_authenticated)





# Shopping Cart Section -----------------------------------------------------------------------


@app.route('/add_to_cart/dessert/<int:dessert_id>', methods=['POST'])
def add_dessert_to_cart(dessert_id):
    dessert = Dessert.query.get_or_404(dessert_id)
    cart_item = {
        'name': dessert.name,
        'price': dessert.price
    }
    cart_items.append(cart_item)
    return jsonify(success=True)

@app.route('/add_to_cart/drink/<int:drink_id>', methods=['POST'])
def add_drink_to_cart(drink_id):
    drink = Drink.query.get_or_404(drink_id)
    cart_item = {
        'name': drink.name,
        'price': drink.price
    }
    cart_items.append(cart_item)
    return jsonify(success=True)

@app.route('/add_to_cart/side/<int:side_id>', methods=['POST'])
def add_side_to_cart(side_id):
    side = side.query.get_or_404(side_id)
    cart_item = {
        'name': side.name,
        'price': side.price
    }
    cart_items.append(cart_item)
    return jsonify(success=True)

@app.route('/add_to_cart/meal_deal/<int:meal_deal_id>', methods=['POST'])
def add_meal_deal_to_cart(meal_deal_id):
    meal_deal = MealDeal.query.get_or_404(meal_deal_id)
    cart_item = {
        'name': meal_deal.name,
        'price': meal_deal.price
    }
    cart_items.append(cart_item)
    return jsonify(success=True)

# ROUTES -------------------------------------------------------------------------------------
@app.route('/about')
def about():
    return render_template('about.html')


# PIZZA LIST-------------------------------------------------------------------
pizzas = [ 
    {'name':'True Italian Pizza', 'image': 'static/Neapolitan-Pizza.jpg.webp','ingredients': 'Soft dough, San Marzano tomatoes, buffalo mozzarella, fresh basil, olive oil. Authentic Italian perfection. '},
    {'name':'Sicilian Pizza',  'image': 'static/Sicilian-Pizza.jpg.webp','ingredients': 'Thick Sicilian crust, robust tomato sauce, generous layer of gooey mozzarella, savory pepperoni rounds. A taste of Sicillian bold flavors.'}, 
    {'name':'Roman-style Pizza', 'image': 'static/Neapolitan-Pizza.jpg.webp','ingredients': 'Crispy Roman crust, fresh tomato sauce, a medley of mozzarella and pecorino cheeses, a hint of basil.'}, 
    {'name':'Staple American Pizza: ','image': 'static/Chicago-Deep-Dish-Pizza.jpg.webp', 'ingredients': 'Buttery deep-dish crust, robust tomato sauce, a hearty layer of mozzarella, spicy Italian sausage, green bell peppers, onions, and a crown of crushed tomatoes.'},
    {'name':'New York-style Pizza','image': 'static/New-York-Style-Pizza.jpg.webp', 'ingredients': 'Thin, foldable crust, tangy tomato sauce, generous mozzarella cheese, a sprinkle of oregano, and a dash of olive oil.'}, 
    {'name': 'Californian Pizza', 'image': 'static/Californian-Pizza.jpg.webp', 'ingredients': 'Thin, artisanal crust, garlic-infused olive oil base, a blend of mozzarella and goat cheese, topped with fresh, vibrant ingredients like sun-dried tomatoes, arugula, and slices of ripe avocado.'}, 
    {'name': 'Detroit Pizza', 'image': 'static/Detroit-Pizza.jpg.webp', 'ingredients': 'Thick, airy Detroit-style crust, brick cheese, rich tomato sauce spread edge-to-edge, pepperoni, and a drizzle of garlic-infused olive oil.'},
    {'name': 'St. Louis Pizza', 'image': 'static/St.-Louis-Pizza.jpg.webp' , 'ingredients':'St. Louis-style thin crust, Provel cheese blend (a mix of cheddar, Swiss, and provolone), sweet and tangy tomato sauce, and a sprinkle of Italian seasoning. A unique twist on pizza perfection.'},
    {'name': 'Canadian Pizza', 'image': 'static/St.-Louis-Pizza.jpg.webp' , 'ingredients':'Classic hand-tossed crust, rich tomato sauce, a blend of mozzarella and cheddar cheese, bacon strips, sliced mushrooms, and a touch of sweet and tangy Canadian bacon.'},
    {'name': 'Mexican Pizza', 'image': 'static/Mexican-Pizza.jpg.webp', 'ingredients': 'Thin, crispy crust, zesty salsa verde base, a blend of melted Monterey Jack and cheddar cheese, seasoned ground beef or chorizo, black beans, diced tomatoes, jalapeños, and a finish of fresh cilantro.'}, 
] 
pizza_sizes = [
    {'name': 'Small', 'price': 10},
    {'name': 'Medium', 'price': 15},
    {'name': 'Large', 'price': 20}, 
]
pizza_bases = [
    {'name': 'Thin Crust', 'price': 2},
    {'name': 'Thick Crust', 'price': 3},
    {'name': 'Gluten-Free', 'price': 5},    
]

@app.route('/menu')
def menu():
    return render_template('menu.html', pizzas=pizzas, pizza_sizes=pizza_sizes, pizza_bases=pizza_bases, cart_items=cart_items)


# SIDES LIST-------------------------------------------------------------------

@app.route('/sides')  
def get_sides(): 
    return render_template('sides.html' , sides=sides)  
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

# DRINKS LIST -------------------------------------------------------------------
@app.route('/drinks')  
def get_drinks():
   return render_template('drinks.html', drinks_data=drinks_data, drink_sizes=drink_sizes) 

drinks_data = [ 
     {'name':'Coca Cola', 'image': 'static/Coca_Cola.jpg'}, 
     {'name':'Coke Zero', 'image': 'static/Coke_Zero.jpg'}, 
     {'name':'Sprite', 'image': 'static/Sprite.jpg'},
     {'name':'Fanta', 'image': 'static/Fanta.jpg'},
     {'name':'L&P', 'image': 'static/L&P.jpg'},
     {'name':'Orange Juice', 'image': 'static/Orange_Juice.jpg'},
     {'name':'Water', 'image': 'static/Water.jpg'},
]
drink_sizes = [
    {'name': '1.5L', 'price': 5.99}, 
    {'name': '600ml', 'price': 3.89},
    {'name': '330ml', 'price': 2.99},
]

meal_deals = [    
    {'name': 'Double Value Deal', 'image': 'Double Value Deal.jpg', 'Description': '2 Large Pizzas & 2 Sides.', 'price': 35.00},
    {'name': 'Triple Value Deal', 'image': 'Triple Value Deal.jpg', 'Description': '3 Large Pizzas & 2 Sides.', 'price': 42.00},   
    {'name': 'Mega Value Deal', 'image': 'Mega Value Deal.jpg', 'Description': '4 Large Pizzas & 2 Sides.', 'price': 49.00}, 
    {'name': 'Chicken Lovers Combo', 'image': 'Chicken Lovers Combo.jpg', 'Description': '1 large Chicken Pizza, Sourn Style Chicken Bites with Ranch Sauce and Garlic Bread.', 'price': 29.00}, 
    {'name': '3 Pizza Deal', 'image': '3 Pizza Deal.jpg', 'Description': '3 Large Classic Value Pizzas.', 'price': 33.00},  
    {'name': '3 Pizzas 3 Sides', 'image': '3 Pizzas 3 Sides.jpg', 'Description': '3 Large Classic Value Pizzas & 3 Sides. Sides include Garlic Bread, Fries or 1.5L Drink.', 'price': 45.00},
    {'name': '4 Pizzas 4 Sides', 'image': '4 Pizzas 4 Sides.jpg', 'Description': '4 Large Classic Value Pizzas & 4 Sides. Sides include Garlic Bread, Fries or 1.5L Drink.', 'price': 33.00},  
]
# MEALS LIST -------------------------------------------------------------------
@app.route('/meal_deals') 
def get_meal_deals():
    return render_template('meal_deals.html', meal_deals=meal_deals) 

desserts_data = [
    {'name': 'Strawberry Cheesecake', 'image': 'static/Strawberry Cheesecake.jpg', 'Description': 'Velvety strawberry cheesecake on a sweet biscuit base.', 'price': 6.39},
    {'name': 'Chocolate Lava Cake', 'image': 'static/Lava Cake.jpg', 'Description': 'Delicious Hershey’s chocolate cake with a warm, rich gooey centre, dusted with icing sugar', 'price': 6.39},
    {'name': 'Chocolate Mousse', 'image': 'static/Chocolate Mousse.jpg', 'Description': 'A decadent, creamy swirl of chocolate mousse.', 'price': 6.39},
    {'name': 'Strawberry Cheesecake', 'image': 'static/Strawberry Cheesecake.jpg', 'Description': 'Velvety strawberry cheesecake on a sweet biscuit base.', 'price': 6.39},
    {'name': 'Ultimate Chocolate Chip Cookie', 'image': 'static/Chocolate Chip Cookie.jpg', 'Description': 'A giant chocolate chip cookie full of rich chocolate chips.', 'price': 9.99},
    {'name': 'Cookie Dough Ice Cream', 'image': 'static/Cookie Dough Ice Cream.jpg', 'price': 16.49},  # Added a default price
]



@app.route('/desserts') 
def show_desserts():
    return render_template('desserts.html', desserts=desserts_data)

@app.route('/checkout')
def show_checkout():
    # Check if the user is logged in
    if 'user_id' in session:
        # Get user details from session
        user_id = session['user_id']
        user_name = session['user_name']
        user_email = session['user_email']

        # Pass user details to the template
        return render_template('checkout.html', user_id=user_id, user_name=user_name, user_email=user_email)
    else:
        # If the user is not logged in, redirect to the login page
        return redirect(url_for('login'))

@app.route('/store_location')
def store_location():
    return render_template('store_location.html')

# logout --------------------------


@app.route('/logout')
def logout():
    # Clear the user session data
    session.clear()
    return render_template('index.html')

@app.route('/')
def index():
    user_authenticated = False  
    return render_template('index.html', user_authenticated=user_authenticated)


@app.route('/initialize_database')
def initialize_database():
    with app.app_context():
        db.create_all()
    return "Database initialized successfully"

        
if __name__ == '__main__':
    app.run(debug=True, port=8080)


