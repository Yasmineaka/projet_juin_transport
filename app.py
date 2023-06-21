from werkzeug.utils import secure_filename


import sqlite3
from flask import Flask, request, render_template , flash
import os
# -----------------------------------------------FORMULAIRE DE RECUPERATION DES DONNÉES DE CONNECTION ET INSCRIPTION-----------------------------------------------------------------------

from flask import Flask, render_template, request, flash, redirect, url_for, session
import sqlite3
import re

app = Flask(__name__)
app.secret_key = "your_secret_key"



app.config['UPLOAD_FOLDER'] = '/Users/imac_p12/Desktop/projet_juin_transport/uploards'

# Configuration de la base de données
DATABASE = "database.db"

def create_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 phone TEXT NOT NULL,
                 password NOT NULL)''')

    conn.commit()
    conn.close()

def backup_database():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    with open("backup.sql", "w") as f:
        for line in conn.iterdump():
            f.write("%s\n" % line)

    conn.close()

create_table()


#----------------------------ROUTE MENU_ACCUEIL------------------------------------------
@app.route('/menu_accueil')
def home():
    return render_template("menu_accueil.html")


#----------------------------ROUTE INSCRIPTION------------------------------------------
@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        password = request.form['password']

        # Vérifier si le nom contient uniquement des lettres ou des mots
        if not name.replace(" ", "").isalpha():
            flash("Le nom doit contenir uniquement des lettres ou des mots.")
            return redirect(url_for('inscription'))

        # Vérifier si le téléphone contient uniquement des chiffres
        if not re.match(r'^[0-9+ ()-]*$', phone):
            flash("Le téléphone contient des caractères invalides.")
            return redirect(url_for('inscription'))

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()

        # Vérifier si l'utilisateur existe déjà
        c.execute("SELECT * FROM users WHERE password=?", (password,))
        user = c.fetchone()

        if user:
            flash("Un utilisateur avec ce mot de passe existe déjà.")
            conn.close()
            return redirect(url_for('inscription'))

        # Insérer l'utilisateur dans la base de données
        c.execute("INSERT INTO users (name, phone, password) VALUES (?, ?, ?)",
                  (name, phone, password))
        conn.commit()
        conn.close()

        flash("Inscription réussie. Vous pouvez maintenant vous connecter.", 'succes')
        backup_database()  # Effectuer la sauvegarde de la base de données
        return redirect(url_for('connexion'))

    return render_template('inscription.html')


#----------------------------ROUTE CONNEXION------------------------------------------
@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == 'POST':
        password = request.form['password']

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()

        # pour vérifier si le mot de passe correspond a un utilisateur
        c.execute("SELECT * FROM users WHERE password=?", (password,))
        user = c.fetchone()

        if user:
            # Enregistrer l'utilisateur dans la session
            session['user_id'] = user[0]
            conn.close()
            return redirect(url_for('home'))
        else:
            flash("Mot de passe incorrect.")
            conn.close()
            return redirect(url_for('connexion'))

    return render_template('connexion.html')



#----------------------------ROUTE A PROPOS------------------------------------------
@app.route('/aPropos')
def aPropos():
    return render_template('a_propos.html')


if __name__ == '__main__':
    app.run(debug=True)

# -----------------------------------------------FIN-----------------------------------------------------------------------





# -----------------------------------------------ROUTE DEMENDE DE LIVREUR-----------------------------------------------------------------------
@app.route('/livraison')
def livraison():
    return render_template('demande_livraison.html')

                            #----------------------ROUTE ADMIN-------------------------

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if username == 'yaka' and password == '1234':
            # Authentification réussie, rediriger vers la page de succès
            flash('Authentification réussie!', 'success')
            return redirect(url_for('admin'))
        else:
            # Authentification échouée, afficher une erreur sur la page de connexion
            flash('Nom d\'utilisateur ou mot de passe incorrect.', 'error')
            return redirect(url_for('login'))
    return render_template('admin_connexion.html')   
                   
                            #----------------------ROUTE ADMIN-------------------------
@app.route('/admin') 
def admin():
    return render_template('admin.html')   







                            #----------------------ROUTE ADMIN LIVRAISON-------------------------
@app.route('/admin_livraison')
def admin_livraison():
    return render_template('admin_livraison.html')

# -----------------------------------------------ROUTE DEMENDE DE MECANICIEN-----------------------------------------------------------------------






# -----------------------------------------------ROUTE RECHERCHE DE CHAUFFEUR-----------------------------------------------------------------------




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



#----------------------------------------ROUTE DEPOT DE DOSSIER---------------------------------------------------
@app.route('/depot_dossier')
def depot_dossier():
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

    return render_template ('succès.html')
    






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

    return render_template ('succès.html')






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


    return render_template ('succès.html')

if __name__ == '__main__':
    app.run(debug=True)







