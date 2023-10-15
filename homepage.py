from flask import Flask, render_template
 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/store_location')
def store_location():
    return render_template('store_location.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True) 
 