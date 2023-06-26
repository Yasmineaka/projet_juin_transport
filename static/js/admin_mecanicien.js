
function validateForm(){
    var nom = document.getElementById("nom");
    var adresse = document.getElementById("adresse");
    var telephone = document.getElementById("telephone");
    var email = document.getElementById("email");
    var dateNaissance = document.getElementById("dateNaissance");
    var experience = document.getElementById("experience");
    var formation = document.getElementById("formation");
    var competences = document.getElementById("competences"); 
    var disponibilite = document.getElementById("disponibilite"); 
    var motivation = document.getElementById("motivation"); 
    var cv = document.getElementById("cv"); 
    var photoIdentite = document.getElementById("photoIdentite"); 
    var diplome = document.getElementById("diplome"); 

    if (nom === "") {
        return false;
      }      

    if (adresse === ""){
        alert("Vous devez entrer un adresse");
        return false;
    }
    if (telephone === ""){
        alert("Vous devez entrer un lieux");
        return false;  
    }
    if (email === ""){
        alert("Veillez entrer un email");
        return false;
    }
   
    if (dateNaissance == ""){
        alert("Vous devez entrer une date de naissance");
        return false;
    }
    if (experience == ""){
        alert("Vous devez entrer une expérience");
        return false;
    }
    if (formation == ""){
        alert("Ce champs ne doit pas etre vide");
        return false;
    }
    if (competences == ""){
        alert("Ce champs ne doit pas etre vide");
        return false;
    }
    if (disponibilite == " "){
        alert("Ce champs ne doit pas etre vide");
        return false;
    }
    if (motivation == ""){
        alert("Vous devez entrer le genre de l'employé");
        return false;
    }
    if (cv == ""){
        alert("Vous devez entrer un fichier");
        return false;
    }
    if (photoIdentite == ""){
        alert("Vous devez entrer un fichier");
        return false;
    }
    if (diplome == ""){
        alert("Vous devez entrer un fichier");
        return false;
    }

    return true;
    // if (date === "" || num_ramassage === "" || lieux_ramassage === "" || num_livraison === "" || commune_liv === "" || montant === "" || contact_depot === "" ) {
    //     alert("Veuillez remplir tous les champs du formulaire.");
    //     event.ElementById(); // Empêche la soumission du formulaire
    // } else{
    // }
}



function showData(){
    var peopleList;
    if(localStorage.getItem("peopleList") == null){
      peopleList = []; 
    }
    else{
        peopleList = JSON.parse(localStorage.getItem("peopleList"))
    }
    var html = "";
    peopleList.forEach(function (element, index){
        html += "<tr>";
        html += "<td>" + element.nom+ "</td>";
        html += "<td>" + element.adresse + "</td>";
        html += "<td>" + element.telephone + "</td>";
        html += "<td>" + element.email+ "</td>";
        html += "<td>" + element.dateNaissance + "</td>";
        html += "<td>" + element.experience + "</td>";
        html += "<td>" + element.formation+ "</td>";
        html += "<td>" + element.competences+ "</td>";
        html += "<td>" + element.disponibilite+ "</td>";
        html += "<td>" + element.motivation+ "</td>";
        html += "<td>" + element.cv+ "</td>";
        html += "<td>" + element.photoIdentite+ "</td>";
        html += 
            '<td><button onclick="deleteData(' +
            index +
            ')" class="btn btn-danger">Delete</button></td>';
        html += "</tr>";
    });
    document.querySelector("#crudTable tbody").innerHTML = 
    html;
}
document.onload = showData();


function addData(){
    if(validateForm()==true){
        var nom = document.getElementById("nom").value;
        var adresse = document.getElementById("adresse").value;
        var telephone = document.getElementById("telephone").value;
        var email = document.getElementById("email").value;
        var dateNaissance = document.getElementById("dateNaissance").value;
        var experience = document.getElementById("experience").value;
        var formation = document.getElementById("formation").value;
        var competences = document.getElementById("competences").value;
        var disponibilite = document.getElementById("disponibilite").value;
        var motivation = document.getElementById("motivation").value;
        var cv = document.getElementById("cv").value;
        var photoIdentite = document.getElementById("photoIdentite").value;
        var diplome = document.getElementById("diplome").value;
       

        var peopleList;
        if (localStorage.getItem("peopleList") == null){
            peopleList = [];
        } else {
            peopleList = JSON.parse(localStorage.getItem
            ("peopleList"));
        }
        peopleList.push({
            nom: nom,
            adresse : adresse,
            telephone : telephone,
            email : email,
            dateNaissance : dateNaissance, 
            experience : experience,
            formation : formation,
            competences : competences,
            disponibilite : disponibilite,
            motivation : motivation,
            cv : cv,
            photoIdentite : photoIdentite,
           diplome :diplome,
        });
        localStorage.setItem("peopleList", JSON.stringify
        (peopleList));
        showData();
        document.getElementById("nom").value = "";
        document.getElementById("adresse").value = "";
        document.getElementById("telephone").value = "";
        document.getElementById("email").value = "";
        document.getElementById("dateNaissance").value = "";
        document.getElementById("experience").value = "";
        document.getElementById("formation").value = "";
        document.getElementById("competences").value = "";
        document.getElementById("disponibilite").value = "";
        document.getElementById("motivation").value = "";
        document.getElementById("cv").value = "";
        document.getElementById("photoIdentite").value = "";
        document.getElementById("diplome").value = "";
    }
}








function deleteData(index){
    var peopleList;
    if (localStorage.getItem("peopleList") == null) {
        peopleList = [];
    } else {
        peopleList= JSON.parse(localStorage.getItem
            ("peopleList"));
    }
    peopleList.splice(index, 1)
    localStorage.setItem("peopleList",JSON.stringify
    (peopleList));
    showData();
}





// function updateData(index){
//     document.getElementById("Submit").style.display = "none";
//     document.getElementById("Update").style.display = "none";

//     var peopleList;
//     if (localStorage.getItem("peopleList")== null){
//         peopleList = [];
//     } else {
//         peopleList = JSON.parse(localStorage.getItem("peopleList"));
//     }
//     document.getElementById("name").value = peopleList[index].nom;
//     document.getElementById("name").value = peopleList[index].prenom;
//     document.getElementById("name").value = peopleList[index].age;
//     document.getElementById("name").value = peopleList[index].sex;
//     document.getElementById("name").value = peopleList[index].contact;

//     document.querySelector("#Update").onclick = function(){
//         if (validateForm == true){
//         peopleList[index].nom = document.getElementById
//         ("nom").value;
//         peopleList[index].prenom = document.getElementById
//         ("prenom").value
//         peopleList[index].age = document.getElementById
//         ("age").value
//         peopleList[index].sex = document.getElementById
//         ("sex").value
//         peopleList[index].contact = document.getElementById
//         ("contact").value;


//         localStorage.setItem("peopleList", JSON.stringify
//         (peopleList));

//         showData();

        
//         document.getElementById("nom").value = "";
//         document.getElementById("prenom").value = "";
//         document.getElementById("age").value = "";
//         document.getElementById("sex").value = "";
//         document.getElementById("contact").value = "";

//         document.getElementById("Submit").style.display =
//         "block";
//         document.getElementById("Update").style.display =
//         "none";
//        }
//     }
// }