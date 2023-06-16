# from flask import Flask, render_template, request


# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def depot_dossier():
#     if request.method == 'POST':
#         nom = request.form['nom']
#         adresse = request.form['adresse']
#         telephone = request.form['telephone']
#         email = request.form['email']
#         dateNaissance = request.form['dateNaissance']
#         experience = request.form['experience']
#         formation = request.form['formation']
#         vehicule = request.form['vehicule']
#         disponibilite = request.form['disponibilite']
#         motivation = request.form['motivation']
        
#         # Stockez les données dans le fichier Jinja nommé 'mma.jinja'
#         with open('templates/admin.jinja', 'w') as file:
#             file.write("{% extends 'base.jinja' %}\n")
#             file.write("{% block content %}\n")
#             file.write(f"<h1>Formulaire de recrutement</h1>\n")
#             file.write(f"<p>Nom complet: {nom}</p>\n")
#             file.write(f"<p>Adresse: {adresse}</p>\n")
#             file.write(f"<p>Numéro de téléphone: {telephone}</p>\n")
#             file.write(f"<p>Adresse e-mail: {email}</p>\n")
#             file.write(f"<p>Date de naissance: {dateNaissance}</p>\n")
#             file.write(f"<p>Expérience en tant que chauffeur: {experience}</p>\n")
#             file.write(f"<p>Formations complémentaires: {formation}</p>\n")
#             file.write(f"<p>Type de véhicule utilisé: {vehicule}</p>\n")
#             file.write(f"<p>Disponibilité: {disponibilite}</p>\n")
#             file.write(f"<p>Motivation: {motivation}</p>\n")
#             file.write("{% endblock %}\n")
        
#         return 'Formulaire soumis avec succès!'
#     else:
#         return render_template('depot_dossier.html')

# if __name__ == '__main__':
#     app.run()




# from flask import Flask, render_template, request, redirect

# app = Flask(__name__)

# # Home page - Menu Accueil
# @app.route('/')
# def menu_accueil():
#     return render_template('menu_accueil.html')

# # inscription page - Connexion
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
    
#     if request.method == 'POST':
#         password = request.form['password']
        
#         # Check if the user is registered (example condition)
#         if password == 'password123':
#             return redirect('/dashboard')  # Redirect to the dashboard page
#         else:
#             error = 'Mot de passe incorrect'
    
#     return render_template('connexion.html', error=error)

# # Registration page - Inscription
# @app.route('/inscription', methods=['GET', 'POST'])
# def inscription():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         # Save the user in the database (example code)
#         # You can use a database library like SQLAlchemy to handle database operations
#         save_user(username, password)
        
#         return redirect('/login')  # Redirect to the login page after successful registration
    
#     return render_template('inscription.html')

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, redirect
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database file
# db = SQLAlchemy(app)

# # Define User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(50))

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

# # Create the database tables
# db.create_all()

# # Home page - Menu Accueil
# @app.route('/')
# def menu_accueil():
#     return render_template('menu_accueil.html')

# # Login page - Connexion
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
    
#     if request.method == 'POST':
#         password = request.form['password']
        
#         # Check if the user is registered
#         user = User.query.filter_by(password=password).first()
#         if user:
#             return redirect('/dashboard')  # Redirect to the dashboard page
#         else:
#             error = 'Mot de passe incorrect'
    
#     return render_template('connexion.html', error=error)

# # Registration page - Inscription
# @app.route('/inscription', methods=['GET', 'POST'])
# def inscription():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         # Save the user in the database
#         user = User(username, password)
#         db.session.add(user)
#         db.session.commit()
        
#         return redirect('/login')  # Redirect to the login page after successful registration
    
#     return render_template('inscription.html')

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, render_template, request, flash, redirect, url_for, session
# import sqlite3

# app = Flask(__name__)
# app.secret_key = "123"

# con = sqlite3.connect("database.db")
# con.execute("CREATE TABLE IF NOT EXISTS customer(emailNumero TEXT, mdp TEXT)")


# @app.route('/')
# def connexion():
#     return render_template('connexion.html')


# @app.route('/inscription', methods=["GET", "POST"])
# def inscription():
#     if request.method == 'POST':
#         password = request.form['mdp']
#         con = sqlite3.connect("database.db")
#         con.row_factory = sqlite3.Row
#         cur = con.cursor()
#         cur.execute("SELECT * FROM customer WHERE mdp=?", (password,))

#         data = cur.fetchone()

#         if data:
#             session["mdp"] = data["mdp"]
#             return redirect("customer")
#         else:
#             flash("Username and Password Mismatch", "danger")
    
#     return redirect(url_for("connexion"))


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         try:
#             emailNumero = request.form['emailNumero']
#             password = request.form['mdp']
#             con = sqlite3.connect("database.db")
#             cur = con.cursor()
#             cur.execute("INSERT INTO customer(emailNumero, mdp) VALUES (?, ?)", (emailNumero, password))
#             con.commit()
#             flash("Record Added Successfully", "success")
#         except Exception as e:
#             print(e)
#             flash("Error in Insert Operation", "danger")
#         finally:
#             con.close()
#             return redirect(url_for("connexion"))

#     return render_template('inscription.html')


# if __name__ ==  '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, flash, redirect, url_for, session
# import sqlite3

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
#                  email TEXT NOT NULL,
#                  password TEXT NOT NULL)''')

#     conn.commit()
#     conn.close()

# create_table()

# @app.route('/')
# def home():
#     return "Bienvenue sur la page d'accueil !"

# @app.route('/inscription', methods=['GET', 'POST'])
# def inscription():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']

#         conn = sqlite3.connect(DATABASE)
#         c = conn.cursor()

#         # Vérifier si l'utilisateur existe déjà
#         c.execute("SELECT * FROM users WHERE email=?", (email,))
#         user = c.fetchone()

#         if user:
#             flash("L'utilisateur existe déjà.")
#             conn.close()
#             return redirect(url_for('inscription'))

#         # Insérer l'utilisateur dans la base de données
#         c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
#         conn.commit()
#         conn.close()

#         flash("Inscription réussie. Vous pouvez maintenant vous connecter.")
#         return redirect(url_for('connexion'))

#     return render_template('inscription.html')

# @app.route('/connexion', methods=['GET', 'POST'])
# def connexion():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         conn = sqlite3.connect(DATABASE)
#         c = conn.cursor()

#         # Vérifier si l'utilisateur existe et que le mot de passe correspond
#         c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
#         user = c.fetchone()

#         if user:
#             # Enregistrer l'utilisateur dans la session
#             session['user_id'] = user[0]
#             session['name'] = user[1]
#             conn.close()
#             return redirect(url_for('home'))
#         else:
#             flash("Identifiants invalides.")
#             conn.close()
#             return redirect(url_for('connexion'))

#     return render_template('connexion.html')

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, flash, redirect, url_for, session
import sqlite3
import re

app = Flask(__name__)
app.secret_key = "your_secret_key"

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
@app.route('/')
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

        flash("Inscription réussie. Vous pouvez maintenant vous connecter.")
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
