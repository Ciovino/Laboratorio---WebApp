# Import module
from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_login import LoginManager
from flask_session import Session
from datetime import datetime
import database_dao as db_dao
from user_model import User

# Create the application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'shh..itsasecret'

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

login_manager = LoginManager()
login_manager.init_app(app)

# Define route and web pages
@app.route('/')
def homepage():
    posts = db_dao.get_all_posts()

    for post in posts:
        post['data_pubblicazione'] = get_giorni_mancanti(post['data_pubblicazione'])

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
    post_completo = db_dao.get_post_by_id(id)

    post = post_completo[0]
    commenti = post_completo[1]

    post['data_pubblicazione'] = get_giorni_mancanti(post['data_pubblicazione'])
    for commento in commenti:
        commento['data_pubblicazione'] = get_giorni_mancanti(commento['data_pubblicazione'])
    
    numcomment = len(commenti)

    return render_template('post.html', post=post, numcomment=numcomment, commenti=commenti)

@app.route('/newcomment', methods=['POST'])
def newComment():
    # testo, id_post
    new_comment = request.form.to_dict()

    # id_utente
    new_comment['id_utente'] = db_dao.get_user_id(session['user'])

    # data_pubblicazione
    new_comment['data_pubblicazione'] = datetime.now().strftime('%Y-%m-%d')

    if not db_dao.add_new_comment(new_comment) :
        flash('Impossibile aggiungere un commento', 'danger')
    else:
        flash('Commento aggiunto correttamente', 'success')

    return redirect(url_for('post', id=new_comment['id_post']))

@app.route('/newpost', methods=['POST'])
def newPost():
    new_post = request.form.to_dict()

    # postid
    new_post['id'] = db_dao.get_next_post_id()

    # fotoPost
    post_image = request.files['immagine_post']

    if post_image :
        post_image_name = 'Immagini/Post/' + str(new_post['id']) + '.png'
        post_image.save('static/' + post_image_name)
    else:
        post_image_name = 'Immagini/Post/_default.png'
    
    new_post['immagine_post'] = post_image_name

    # user id
    new_post['id_utente'] = db_dao.get_user_id(session['user'])

    # giorniFa
    data_form = new_post.get('data_pubblicazione')

    if data_form > datetime.now().strftime('%Y-%m-%d'):
        # Data non valida
        flash('Impossibile creare il post', 'danger')
        return redirect(url_for('homepage'))

    new_post['data_pubblicazione'] = data_form

    if not db_dao.add_new_post(new_post) :
        flash('Impossibile creare il post', 'danger')
    else:
        flash('Post creato correttamente', 'success')
        
    return redirect(url_for('homepage'))

@login_manager.user_loader
def user_load(user_id):
    user_from_db = db_dao.get_user_by_id(user_id)

    user = User(user_from_db['id'], user_from_db['nickname'], user_from_db['password'], user_from_db['immagine_profilo'])

    return user

# Calcolo di quanti giorni sono passati dalla pubblicazione del post
def get_giorni_mancanti(data):
    giorni = (datetime.now() - datetime.strptime(data, '%Y-%m-%d')).days

    if giorni == 0:
        return 'Oggi'
    elif giorni == 1:
        return 'Ieri'
    else:
        return f'{giorni} giorni fa'
