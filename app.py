# Import module
from flask import Flask, render_template

# Create the application
app = Flask(__name__)

# Define route and web pages
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/presentazione.html')
def presentazione():
    return render_template('presentazione.html')