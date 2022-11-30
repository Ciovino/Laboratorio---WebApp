# Import module
from flask import Flask, render_template, redirect, url_for, session, request
from flask_session import Session

# Create the application
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

posts = [{'id': 1, 'fotoPost':'Immagini/img1.jpg', 'fotoProfilo':'Immagini/Profilo.png', 'username':'luigi', 'giorniFa':2, 
            'contenuto':'''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec mollis enim ut egestas lacinia. 
            Vestibulum sodales at odio non semper. Donec mattis pellentesque rutrum.'''},
        {'id': 2, 'fotoPost':'Immagini/img2.jpg', 'fotoProfilo':'Immagini/Profilo.png', 'username':'alberto', 'giorniFa':4,
            'contenuto':'''Nullam nunc eros, sagittis eu gravida vel, interdum a tellus. Praesent quis lectus semper, 
            interdum mauris eu, molestie ligula. Morbi sagittis ullamcorper blandit.'''},
        {'id': 3, 'fotoPost':'Immagini/img3.jpg', 'fotoProfilo':'Immagini/Profilo.png', 'username':'juan', 'giorniFa':4, 
            'contenuto':'''Vestibulum quis lectus nec odio mollis consectetur vel non libero. In ac leo dolor. Nunc 
            consequat quam et leo pretium porta.'''}]

# Define route and web pages
@app.route('/')
def homepage():
    return render_template('homepage.html', posts=posts)

@app.route('/login', methods=['POST', 'GET'])
def user_login():
    session['login'] = True
    session['user'] = request.form.get('user-login')
    return redirect(url_for('homepage'))

@app.route('/presentazione.html')
def presentazione():
    return render_template('presentazione.html')

@app.route('/posts/<int:id>')
def post(id):
    post = [p for p in posts if p['id'] == id][0]
    return render_template('post.html', post=post)