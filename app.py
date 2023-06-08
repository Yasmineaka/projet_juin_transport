from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def depot_dossier():
    if request.method == 'POST':
        nom = request.form['nom']
        adresse = request.form['adresse']
        telephone = request.form['telephone']
        email = request.form['email']
        dateNaissance = request.form['dateNaissance']
        experience = request.form['experience']
        formation = request.form['formation']
        vehicule = request.form['vehicule']
        disponibilite = request.form['disponibilite']
        motivation = request.form['motivation']
        
        # Stockez les données dans le fichier Jinja nommé 'mma.jinja'
        with open('templates/admin.jinja', 'w') as file:
            file.write("{% extends 'base.jinja' %}\n")
            file.write("{% block content %}\n")
            file.write(f"<h1>Formulaire de recrutement</h1>\n")
            file.write(f"<p>Nom complet: {nom}</p>\n")
            file.write(f"<p>Adresse: {adresse}</p>\n")
            file.write(f"<p>Numéro de téléphone: {telephone}</p>\n")
            file.write(f"<p>Adresse e-mail: {email}</p>\n")
            file.write(f"<p>Date de naissance: {dateNaissance}</p>\n")
            file.write(f"<p>Expérience en tant que chauffeur: {experience}</p>\n")
            file.write(f"<p>Formations complémentaires: {formation}</p>\n")
            file.write(f"<p>Type de véhicule utilisé: {vehicule}</p>\n")
            file.write(f"<p>Disponibilité: {disponibilite}</p>\n")
            file.write(f"<p>Motivation: {motivation}</p>\n")
            file.write("{% endblock %}\n")
        
        return 'Formulaire soumis avec succès!'
    else:
        return render_template('depot_dossier.html')

if __name__ == '__main__':
    app.run()




