
# # -----------------------------------------------FORMULAIRE DE RECUPERATION DES DONNÉES DE CONNECTION ET INSCRIPTION-----------------------------------------------------------------------

# from flask import Flask, render_template, request, flash, redirect, url_for, session
# import sqlite3
# import re

# app = Flask(__name__)
# app.secret_key = "your_secret_key"

# # Configuration de la base de données
# DATABASE = "database.db"

# def create_table():
#     conn = sqlite3.connect(DATABASE)
#     c = conn.cursor()

#     c.execute('''CREATE TABLE IF NOT EXISTS users
#                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  name TEXT NOT NULL,
#                  phone TEXT NOT NULL,
#                  password NOT NULL)''')

#     conn.commit()
#     conn.close()

# def backup_database():
#     conn = sqlite3.connect(DATABASE)
#     c = conn.cursor()

#     with open("backup.sql", "w") as f:
#         for line in conn.iterdump():
#             f.write("%s\n" % line)

#     conn.close()

# create_table()


# #----------------------------ROUTE MENU_ACCUEIL------------------------------------------
# @app.route('/')
# def home():
#     return render_template("menu_accueil.html")


# #----------------------------ROUTE INSCRIPTION------------------------------------------
# @app.route('/inscription', methods=['GET', 'POST'])
# def inscription():
#     if request.method == 'POST':
#         name = request.form['name']
#         phone = request.form['phone']
#         password = request.form['password']

#         # Vérifier si le nom contient uniquement des lettres ou des mots
#         if not name.replace(" ", "").isalpha():
#             flash("Le nom doit contenir uniquement des lettres ou des mots.")
#             return redirect(url_for('inscription'))

#         # Vérifier si le téléphone contient uniquement des chiffres
#         if not re.match(r'^[0-9+ ()-]*$', phone):
#             flash("Le téléphone contient des caractères invalides.")
#             return redirect(url_for('inscription'))

#         conn = sqlite3.connect(DATABASE)
#         c = conn.cursor()

#         # Vérifier si l'utilisateur existe déjà
#         c.execute("SELECT * FROM users WHERE password=?", (password,))
#         user = c.fetchone()

#         if user:
#             flash("Un utilisateur avec ce mot de passe existe déjà.")
#             conn.close()
#             return redirect(url_for('inscription'))

#         # Insérer l'utilisateur dans la base de données
#         c.execute("INSERT INTO users (name, phone, password) VALUES (?, ?, ?)",
#                   (name, phone, password))
#         conn.commit()
#         conn.close()

#         flash("Inscription réussie. Vous pouvez maintenant vous connecter.")
#         backup_database()  # Effectuer la sauvegarde de la base de données
#         return redirect(url_for('connexion'))

#     return render_template('inscription.html')


# #----------------------------ROUTE CONNEXION------------------------------------------
# @app.route('/connexion', methods=['GET', 'POST'])
# def connexion():
#     if request.method == 'POST':
#         password = request.form['password']

#         conn = sqlite3.connect(DATABASE)
#         c = conn.cursor()

#         # pour vérifier si le mot de passe correspond a un utilisateur
#         c.execute("SELECT * FROM users WHERE password=?", (password,))
#         user = c.fetchone()

#         if user:
#             # Enregistrer l'utilisateur dans la session
#             session['user_id'] = user[0]
#             conn.close()
#             return redirect(url_for('home'))
#         else:
#             flash("Mot de passe incorrect.")
#             conn.close()
#             return redirect(url_for('connexion'))

#     return render_template('connexion.html')



# #----------------------------ROUTE A PROPOS------------------------------------------
# @app.route('/aPropos')
# def aPropos():
#     return render_template('a_propos.html')


# if __name__ == '__main__':
#     app.run(debug=True)

#  -----------------------------------------------FIN-----------------------------------------------------------------------

# from flask import Flask, render_template, request
# import sqlite3
# import os

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads'  # Dossier pour enregistrer les fichiers uploadés

# # Connexion à la base de données SQLite
# conn = sqlite3.connect('database.db', check_same_thread=False)
# cursor = conn.cursor()

# # Création de la table conducteur
# cursor.execute('''CREATE TABLE IF NOT EXISTS conducteur
#                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   nom TEXT,
#                   adresse TEXT,
#                   telephone TEXT,
#                   email TEXT,
#                   date_naissance TEXT,
#                   categorie_permis TEXT,
#                   date_obtention_permis TEXT,
#                   pays_emission_permis TEXT,
#                   responsabilites TEXT,
#                   motivation TEXT,
#                   cv TEXT,
#                   photo_identite TEXT,
#                   copie_permis TEXT)''')

# # Création de la table livreur_moto
# cursor.execute('''CREATE TABLE IF NOT EXISTS livreur_moto
#                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   nom TEXT,
#                   adresse TEXT,
#                   telephone TEXT,
#                   email TEXT,
#                   disponibilite TEXT,
#                   experience TEXT,
#                   formation TEXT,
#                   permis TEXT,
#                   competences TEXT,
              
#                   motivation TEXT,
#                   salaire TEXT,
#                   commentaires TEXT)''')
#   #   references TEXT,
# # Création de la table chauffeur_vtc
# cursor.execute('''CREATE TABLE IF NOT EXISTS chauffeur_vtc
#                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   nom TEXT,
#                   adresse TEXT,
#                   telephone TEXT,
#                   email TEXT,
#                   date_naissance TEXT,
#                   experience TEXT,
#                   formation TEXT,
#                   vehicule TEXT,
#                   disponibilite TEXT,
#                   motivation TEXT,
#                   cv TEXT,
#                   photo_identite TEXT,
#                   permis TEXT)''')

# # Création de la table mecanicien
# cursor.execute('''CREATE TABLE IF NOT EXISTS mecanicien
#                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   nom TEXT,
#                   adresse TEXT,
#                   telephone TEXT,
#                   email TEXT,
#                   date_naissance TEXT,
#                   experience TEXT,
#                   formation TEXT,
#                   competences TEXT,
#                   disponibilite TEXT,
#                   motivation TEXT,
#                   cv TEXT,
#                   photo_identite TEXT,
#                   diplome TEXT)''')

# # Page d'accueil
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route pour le formulaire du conducteur
# @app.route('/conducteur', methods=['POST','GET'])
# def conducteur():
#     if request.method == 'POST':
#         # Récupérer les données du formulaire
#         nom = request.form['nom']
#         adresse = request.form['adresse']
#         telephone = request.form['telephone']
#         email = request.form['email']
#         date_naissance = request.form['dateNaissance']
#         categorie_permis = request.form['categoriePermis']
#         date_obtention_permis = request.form['dateObtentionPermis']
#         pays_emission_permis = request.form['paysEmissionPermis']
#         responsabilites = request.form['responsabilites']
#         motivation = request.form['motivation']
#         cv = save_file(request.files['cv'])
#         photo_identite = save_file(request.files['photoIdentite'])
#         copie_permis = save_file(request.files['copiePermis'])

#         # Insérer les données dans la base de données
#         cursor.execute('''INSERT INTO conducteur
#                           (nom, adresse, telephone, email, date_naissance, categorie_permis,
#                           date_obtention_permis, pays_emission_permis, responsabilites,
#                           motivation, cv, photo_identite, copie_permis)
#                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#                        (nom, adresse, telephone, email, date_naissance, categorie_permis,
#                         date_obtention_permis, pays_emission_permis, responsabilites,
#                         motivation, cv, photo_identite, copie_permis))
#         conn.commit()

#         return render_template('success.html')

# # Route pour le formulaire du livreur moto
# @app.route('/livreur_moto', methods=['POST'])
# def livreur_moto():
#     if request.method == 'POST':
#         # Récupérer les données du formulaire
#         nom = request.form['nom']
#         adresse = request.form['adresse']
#         telephone = request.form['telephone']
#         email = request.form['email']
#         disponibilite = request.form['disponibilite']
#         experience = request.form['experience']
#         formation = request.form['formation']
#         permis = request.form['permis']
#         competences = request.form['competences']
#         references = request.form['references']
#         motivation = request.form['motivation']
#         salaire = request.form['salaire']
#         commentaires = request.form['commentaires']

#         # Insérer les données dans la base de données
#         cursor.execute('''INSERT INTO livreur_moto
#                           (nom, adresse, telephone, email, disponibilite, experience,
#                           formation, permis, competences, references, motivation,
#                           salaire, commentaires)
#                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#                        (nom, adresse, telephone, email, disponibilite, experience,
#                         formation, permis, competences, references, motivation,
#                         salaire, commentaires))
#         conn.commit()

#         return render_template('success.html')

# # Route pour le formulaire du chauffeur VTC
# @app.route('/chauffeur_vtc', methods=['POST'])
# def chauffeur_vtc():
#     if request.method == 'POST':
#         # Récupérer les données du formulaire
#         nom = request.form['nom']
#         adresse = request.form['adresse']
#         telephone = request.form['telephone']
#         email = request.form['email']
#         date_naissance = request.form['dateNaissance']
#         experience = request.form['experience']
#         formation = request.form['formation']
#         vehicule = request.form['vehicule']
#         disponibilite = request.form['disponibilite']
#         motivation = request.form['motivation']
#         cv = save_file(request.files['cv'])
#         photo_identite = save_file(request.files['photoIdentite'])
#         permis = request.form['permis']

#         # Insérer les données dans la base de données
#         cursor.execute('''INSERT INTO chauffeur_vtc
#                           (nom, adresse, telephone, email, date_naissance, experience,
#                           formation, vehicule, disponibilite, motivation, cv,
#                           photo_identite, permis)
#                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#                        (nom, adresse, telephone, email, date_naissance, experience,
#                         formation, vehicule, disponibilite, motivation, cv,
#                         photo_identite, permis))
#         conn.commit()

#         return render_template('success.html')

# # Route pour le formulaire du mécanicien
# @app.route('/mecanicien', methods=['POST'])
# def mecanicien():
#     if request.method == 'POST':
#         # Récupérer les données du formulaire
#         nom = request.form['nom']
#         adresse = request.form['adresse']
#         telephone = request.form['telephone']
#         email = request.form['email']
#         date_naissance = request.form['dateNaissance']
#         experience = request.form['experience']
#         formation = request.form['formation']
#         competences = request.form['competences']
#         disponibilite = request.form['disponibilite']
#         motivation = request.form['motivation']
#         cv = save_file(request.files['cv'])
#         photo_identite = save_file(request.files['photoIdentite'])
#         diplome = request.form['diplome']

#         # Insérer les données dans la base de données
#         cursor.execute('''INSERT INTO mecanicien
#                           (nom, adresse, telephone, email, date_naissance, experience,
#                           formation, competences, disponibilite, motivation, cv,
#                           photo_identite, diplome)
#                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#                        (nom, adresse, telephone, email, date_naissance, experience,
#                         formation, competences, disponibilite, motivation, cv,
#                         photo_identite, diplome))
#         conn.commit()

#         return render_template('success.html')

# # Fonction pour enregistrer un fichier
# def save_file(file):
#     if file:
#         filename = file.filename
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         return filename
#     return None

# if __name__ == '__main__':
#     app.run()




from werkzeug.utils import secure_filename


import sqlite3
from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/Users/imac_p12/Desktop/projet_juin_transport/uploards'



# Créer la base de données et les tables nécessaires
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Table pour le formulaire Conducteur
cursor.execute('''CREATE TABLE IF NOT EXISTS conducteur
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nom TEXT,
                   adresse TEXT,
                   telephone TEXT,
                   email TEXT,
                   dateNaissance DATE,
                   categoriePermis TEXT,
                   dateObtentionPermis DATE,
                   paysEmissionPermis TEXT,
                   responsabilites TEXT,
                   motivation TEXT,
                   cv BLOB,
                   photoIdentite BLOB,
                   copiePermis BLOB,
                   cv_filename BLOB,
                   photoIdentite_filename,
                   copiePermis_filename)''')

# Table pour le formulaire Moto
cursor.execute('''CREATE TABLE IF NOT EXISTS moto
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nomMoto TEXT,
                   adresseMoto TEXT,
                   telephoneMoto TEXT,
                   emailMoto TEXT,
                   disponibiliteMoto TEXT,
                   experienceMoto TEXT,
                   formationMoto TEXT,
                   permisMoto TEXT,
                   competencesMoto TEXT,
                   referencesMoto TEXT,
                   motivationMoto TEXT,
                   salaireMoto TEXT,
                   commentairesMoto TEXT)''')

# Table pour le formulaire Chauffeur VTC
cursor.execute('''CREATE TABLE IF NOT EXISTS chauffeur_vtc
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nom TEXT,
                   adresse TEXT,
                   telephone TEXT,
                   email TEXT,
                   dateNaissance DATE,
                   experience TEXT,
                   formation TEXT,
                   vehicule TEXT,
                   disponibilite TEXT,
                   motivation TEXT,
                   cv BLOB,
                   photoIdentite BLOB,
                   cv_filename BLOB,
                   photoIdentite_filename BLOB,
                   permis_filename BLOB,
                   permis BLOB)''')

# Table pour le formulaire Mécanicien
cursor.execute('''CREATE TABLE IF NOT EXISTS mecanicien
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nom TEXT,
                   adresse TEXT,
                   telephone TEXT,
                   email TEXT,
                   dateNaissance DATE,
                   experience TEXT,
                   formation TEXT,
                   competences TEXT,
                   disponibilite TEXT,
                   motivation TEXT,
                   cv BLOB,
                   photoIdentite BLOB,
                   diplome BLOB,
                   cv_filename BLOB,
                   photoIdentite_filename BLOB,
                   diplome_filename BLOB)''')

conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('depot_dossier.html')



#----------------------------------------DOSSIER CHAUFFEURS VTC---------------------------------------------------
@app.route('/process_conducteur', methods=['POST', 'GET'])
def process_conducteur():
    # Récupérer les données du formulaire Conducteur
    nom = request.form.get('nom')
    adresse = request.form.get('adresse')
    telephone = request.form.get('telephone')
    email = request.form.get('email')
    dateNaissance = request.form.get('dateNaissance')
    categoriePermis = request.form.get('categoriePermis')
    dateObtentionPermis = request.form.get('dateObtentionPermis')
    paysEmissionPermis = request.form.get('paysEmissionPermis')
    responsabilites = request.form.get('responsabilites')
    motivation = request.form.get('motivation')
    cv_file = request.files['cv']
    photoIdentite_file = request.files['photoIdentite']
    copiePermis_file = request.files['copiePermis']

    # Gérer les fichiers téléchargés
    cv_filename = secure_filename(cv_file.filename) if cv_file else None
    photoIdentite_filename = secure_filename(photoIdentite_file.filename) if photoIdentite_file else None
    copiePermis_filename = secure_filename(copiePermis_file.filename) if copiePermis_file else None

    # Convertir les fichiers téléchargés en données binaires
    cv_data = cv_file.read() if cv_file else None
    photoIdentite_data = photoIdentite_file.read() if photoIdentite_file else None
    copiePermis_data = copiePermis_file.read() if copiePermis_file else None

    # Insérer les données dans la base de données
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO conducteur (nom, adresse, telephone, email, dateNaissance, categoriePermis, dateObtentionPermis, paysEmissionPermis, responsabilites, motivation, cv, photoIdentite, copiePermis, cv_filename, photoIdentite_filename, copiePermis_filename)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (nom, adresse, telephone, email, dateNaissance, categoriePermis, dateObtentionPermis, paysEmissionPermis, responsabilites, motivation, cv_data, photoIdentite_data, copiePermis_data, cv_filename, photoIdentite_filename, copiePermis_filename))
    conn.commit()
    conn.close()

    # Enregistrer les fichiers téléchargés s'ils existent
    if cv_file:
        cv_file.save(os.path.join(app.config['UPLOAD_FOLDER'], cv_filename))
    if photoIdentite_file:
        photoIdentite_file.save(os.path.join(app.config['UPLOAD_FOLDER'], photoIdentite_filename))
    if copiePermis_file:
        copiePermis_file.save(os.path.join(app.config['UPLOAD_FOLDER'], copiePermis_filename))

    return 'Formulaire Conducteur soumis avec succès!'







@app.route('/process_moto', methods=['POST','GET'])
def process_moto():
    # Récupérer les données du formulaire Moto
    nomMoto = request.form.get('nomMoto')
    adresseMoto = request.form.get('adresseMoto')
    telephoneMoto = request.form.get('telephoneMoto')
    emailMoto = request.form.get('emailMoto')
    disponibiliteMoto = request.form.get('disponibiliteMoto')
    experienceMoto = request.form.get('experienceMoto')
    formationMoto = request.form.get('formationMoto')
    permisMoto = request.form.get('permisMoto')
    competencesMoto = request.form.get('competencesMoto')
    referencesMoto = request.form.get('referencesMoto')
    motivationMoto = request.form.get('motivationMoto')
    salaireMoto = request.form.get('salaireMoto')
    commentairesMoto = request.form.get('commentairesMoto')
    

    # Insérer les données dans la base de données
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO moto (nomMoto, adresseMoto, telephoneMoto, emailMoto, disponibiliteMoto, experienceMoto, formationMoto, permisMoto, competencesMoto, referencesMoto, motivationMoto, salaireMoto, commentairesMoto)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (nomMoto, adresseMoto, telephoneMoto, emailMoto, disponibiliteMoto, experienceMoto, formationMoto, permisMoto, competencesMoto, referencesMoto, motivationMoto, salaireMoto, commentairesMoto))
    conn.commit()
    conn.close()


# #----------------------------ROUTE CONNEXION------------------------------------------
# @app.route('/connexion', methods=['GET', 'POST'])
# def connexion():
#     if request.method == 'POST':
#         password = request.form['password']
    
# #----------------------------ROUTE CONNEXION------------------------------------------
# @app.route('/connexion', methods=['GET', 'POST'])
# def connexion():
#     if request.method == 'POST':
#         password = request.form['password']

#     return 'Formulaire Moto soumis avec succès!'






#----------------------------------------DOSSIER CHAUFFEURS VTC---------------------------------------------------
@app.route('/process_chauffeur_vtc', methods=['POST','GET'])
def process_chauffeur_vtc():
    # Récupérer les données du formulaire Chauffeur VTC
    nom = request.form.get('nom')
    adresse = request.form.get('adresse')
    telephone = request.form.get('telephone')
    email = request.form.get('email')
    dateNaissance = request.form.get('dateNaissance')
    experience = request.form.get('experience')
    formation = request.form.get('formation')
    vehicule = request.form.get('vehicule')
    disponibilite = request.form.get('disponibilite')
    motivation = request.form.get('motivation')
    cv = request.files['cv']
    photoIdentite = request.files['photoIdentite']
    permis = request.files['permis']
    # Gérer les fichiers téléchargés
    cv_filename = secure_filename(cv.filename) if cv else None
    photoIdentite_filename = secure_filename(photoIdentite.filename) if photoIdentite else None
    permis_filename = secure_filename(permis.filename) if permis else None

    # Insérer les données dans la base de données
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO chauffeur_vtc (nom, adresse, telephone, email, dateNaissance, experience, formation, vehicule, disponibilite, motivation, cv_filename, photoIdentite_filename, permis_filename)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (nom, adresse, telephone, email, dateNaissance, experience, formation, vehicule, disponibilite, motivation, cv_filename, photoIdentite_filename, permis_filename))
    conn.commit()
    conn.close()

    # Enregistrer les fichiers téléchargés s'ils existent
    if cv:
        cv.save(os.path.join(app.config['UPLOAD_FOLDER'], cv_filename))
    if photoIdentite:
        photoIdentite.save(os.path.join(app.config['UPLOAD_FOLDER'], photoIdentite_filename))
    if permis:
        permis.save(os.path.join(app.config['UPLOAD_FOLDER'], permis_filename))

    return 'Formulaire Chauffeur VTC soumis avec succès!'






#----------------------------------------DOSSIER MECANICIEN ---------------------------------------------------
@app.route('/process_mecanicien', methods=['POST'])
def process_mecanicien():
    # Récupérer les données du formulaire Mécanicien
    nom = request.form.get('nom')
    adresse = request.form.get('adresse')
    telephone = request.form.get('telephone')
    email = request.form.get('email')
    dateNaissance = request.form.get('dateNaissance')
    experience = request.form.get('experience')
    formation = request.form.get('formation')
    competences = request.form.get('competences')
    disponibilite = request.form.get('disponibilite')
    motivation = request.form.get('motivation')
    cv = request.files['cv']
    photoIdentite = request.files['photoIdentite']
    diplome = request.files['diplome']
    # Gérer les fichiers téléchargés
    cv_filename = secure_filename(cv.filename) if cv else None
    photoIdentite_filename = secure_filename(photoIdentite.filename) if photoIdentite else None
    diplome_filename = secure_filename(diplome.filename) if diplome else None


   # Convertir les fichiers téléchargés en données binaires
    cv_data = cv.read() if cv else None
    photoIdentite_data = photoIdentite.read() if photoIdentite else None
    diplome_data = diplome.read() if diplome else None
    # Insérer les données dans la base de données
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO mecanicien (nom, adresse, telephone, email, dateNaissance, experience, formation, competences, disponibilite, motivation, cv, photoIdentite,  diplome, cv_filename, photoIdentite_filename, diplome_filename)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (nom, adresse, telephone, email, dateNaissance, experience, formation, competences, disponibilite, motivation, cv_data, photoIdentite_data, diplome_data, cv_filename,  photoIdentite_filename,  diplome_filename))
    conn.commit()
    conn.close()

    # Enregistrer les fichiers téléchargés s'ils existent
    if cv:
        cv.save(os.path.join(app.config['UPLOAD_FOLDER'], cv_filename))
    if photoIdentite:
        photoIdentite.save(os.path.join(app.config['UPLOAD_FOLDER'], photoIdentite_filename))
    if diplome:
        diplome.save(os.path.join(app.config['UPLOAD_FOLDER'], diplome_filename))


    return 'Formulaire Mécanicien soumis avec succès!'

if __name__ == '__main__':
    app.run(debug=True)
