import sqlite3

# Recupera tutti i post dal database
def get_all_posts():
    # Crea una connessione al database
    connection = sqlite3.connect('databases/social.database.db')
    connection.row_factory = sqlite3.Row

    # Crea un cursore
    cursor = connection.cursor()

    # Query sql
    query = '''SELECT u.nickname, p.id, p.immagine_post, u.immagine_profilo, p.data_pubblicazione, p.testo 
            FROM utenti u, post p 
            WHERE u.id = p.id_utente'''

    # Esegui query
    cursor.execute(query)

    # Recupera risultati
    posts = cursor.fetchall()

    # Chiudi connessione e cursore
    cursor.close()
    connection.close()

    return posts

# Recupera post con id
def get_post_by_id(id):
    # Crea una connessione al database
    connection = sqlite3.connect('databases/social.database.db')
    connection.row_factory = sqlite3.Row

    # Crea un cursore
    cursor = connection.cursor()

    # Query sql
    query = '''SELECT u.nickname, p.id, p.immagine_post, u.immagine_profilo, p.data_pubblicazione, p.testo
            FROM utenti u, post p
            WHERE p.id = ? AND u.id = p.id_utente'''

    # Esegui query
    cursor.execute(query, (id,))

    # Recupera risultati
    post = cursor.fetchone()

    # Chiudi connessione e cursore
    cursor.close()
    connection.close()
    
    return post

def get_next_post_id():
    # Crea una connessione al database
    connection = sqlite3.connect('databases/social.database.db')

    # Crea un cursore
    cursor = connection.cursor()

    query = 'SELECT MAX(id) FROM post'

    cursor.execute(query)

    id = cursor.fetchone()

    # Chiudi connessione e cursore
    cursor.close()
    connection.close()

    return int(id[0]) + 1

def get_user_id(nickname):
    # Crea una connessione al database
    connection = sqlite3.connect('databases/social.database.db')

    # Crea un cursore
    cursor = connection.cursor()

    query = 'SELECT id FROM utenti WHERE nickname = ?'

    cursor.execute(query, (nickname,))

    id = cursor.fetchone()

    # Chiudi connessione e cursore
    cursor.close()
    connection.close()

    return int(id[0])

def add_new_post(post):
    # Crea una connessione al database
    connection = sqlite3.connect('databases/social.database.db')
    connection.row_factory = sqlite3.Row

    # Crea un cursore
    cursor = connection.cursor()

    # Query
    query = '''INSERT INTO post(data_pubblicazione, testo, immagine_post, id_utente) VALUES(?,?,?,?)'''

    success = False

    try:
        cursor.execute(query, (post['data_pubblicazione'], post['testo'], post['immagine_post'], post['id_utente']))
        connection.commit()
        success = True
    except Exception as e:
        print('ERROR', str(e))
        # if something goes wrong: rollback
        connection.rollback()

    # Chiudi connessione e cursore
    cursor.close()
    connection.close()

    return success
