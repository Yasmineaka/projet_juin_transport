from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/depot_dossier', methods=['GET', 'POST'])
def depot_dossier():
    if request.method == 'POST':
        data = {
                'nom':request.form['nom'],
                'adresse': request.form['adresse'],
                'telephone' : request.form['telephone'],
                'email' :request.form['email'],
                'date_naissance' : request.form['dateNaissance'],
                'categorie_permis' : request.form['categoriePermis'],
                'date_obtention_permis' :request.form['dateObtentionPermis'],
                'pays_emission_permis':request.form['paysEmissionPermis'],
                'responsabilites' :request.form['responsabilites'],
                'motivation' : request.form['motivation'],
                'cv': request.files['cv'],
                'photo_identite':request.files['photoIdentite'],
                'copie_permis' : request.files['copiePermis']
        }

        data=['nom','adresse','telephone','email','date_naissance','categorie_permis','date_obtention_permis','pays_emission_permis',]  
        # Faites quelque chose avec les données récupérées, par exemple les enregistrer dans une base de données
        
        return render_template('admin.html', data=data)
    return render_template('depot_dossier.html')










if __name__ == '__main__':
    app.run()



