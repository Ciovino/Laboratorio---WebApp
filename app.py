# Import module
from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_session import Session
from datetime import datetime

# Create the application
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

posts = [{'id': 1, 'fotoPost':'Immagini/img1.jpg', 'fotoProfilo':'Immagini/Profilo.png', 'username':'luigi', 'giorniFa':'2 giorni fa', 
            'contenuto':'''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec mollis enim ut egestas lacinia. 
            Vestibulum sodales at odio non semper. Donec mattis pellentesque rutrum.'''},
        {'id': 2, 'fotoPost':'Immagini/img2.jpg', 'fotoProfilo':'Immagini/Profilo.png', 'username':'alberto', 'giorniFa':'4 giorni fa',
            'contenuto':'''Nullam nunc eros, sagittis eu gravida vel, interdum a tellus. Praesent quis lectus semper, 
            interdum mauris eu, molestie ligula. Morbi sagittis ullamcorper blandit.'''},
        {'id': 3, 'fotoPost':'Immagini/img3.jpg', 'fotoProfilo':'Immagini/Profilo.png', 'username':'juan', 'giorniFa':'4 giorni fa', 
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

@app.route('/newpost', methods=['POST'])
def newPost():
    new_post = request.form.to_dict()

    # postid
    new_post['id'] = posts[-1]['id'] + 1

    # fotoPost
    post_image = request.files['fotoPost']

    if post_image :
        post_image_name = 'Immagini/img' + new_post['id'] + '.jpg'
        post_image.save('static/' + post_image_name)
    else:
        post_image_name = 'Immagini/foto.png'
    
    new_post['fotoPost'] = post_image_name

    # fotoProfilo
    new_post['fotoProfilo'] = 'Immagini/Profilo.png'

    # username
    new_post['username'] = session['user']

    # giorniFa
    data_form = new_post.get('giorniFa')

    if data_form > datetime.now().strftime('%Y-%m-%d'):
        # Data non valida
        flash('Impossibile creare il post', 'danger')
        return redirect(url_for('homepage'))
    else:
        # Calcolare quanti giorni sono passati dalla pubblicazione del post
        dataPost = datetime.strptime(data_form, '%Y-%m-%d')
        giorni = datetime.now() - dataPost

        if giorni.days == 1:
            new_post['giorniFa'] = 'Ieri'
        elif giorni.days == 0:
            new_post['giorniFa'] = 'Oggi'
        else:
            new_post['giorniFa'] = f'{giorni.days} giorni fa'

    posts.append(new_post)
    
    flash('Post creato correttamente', 'success')
    return redirect(url_for('homepage'))