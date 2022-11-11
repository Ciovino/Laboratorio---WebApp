# Import module
from flask import Flask, render_template

# Create the application
app = Flask(__name__)

# Define route and web pages
@app.route('/')
def homepage():
    posts = [{'fotoPost':'Immagini/img1.jpg', 'fotoProfilo':'Immagini/Profilo.png', 'username':'luigi', 'giorniFa':2, 
                'contenuto':'''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec mollis enim ut egestas lacinia. 
                Vestibulum sodales at odio non semper. Donec mattis pellentesque rutrum.'''},
            {'fotoPost':'Immagini/img2.jpg', 'fotoProfilo':'Immagini/Profilo.png', 'username':'alberto', 'giorniFa':4,
                'contenuto':'''Nullam nunc eros, sagittis eu gravida vel, interdum a tellus. Praesent quis lectus semper, 
                interdum mauris eu, molestie ligula. Morbi sagittis ullamcorper blandit.'''},
            {'fotoPost':'Immagini/img3.jpg', 'fotoProfilo':'Immagini/Profilo.png', 'username':'juan', 'giorniFa':4, 
                'contenuto':'''Vestibulum quis lectus nec odio mollis consectetur vel non libero. In ac leo dolor. Nunc 
                consequat quam et leo pretium porta.'''}]

    return render_template('homepage.html', posts=posts)

@app.route('/presentazione.html')
def presentazione():
    return render_template('presentazione.html')