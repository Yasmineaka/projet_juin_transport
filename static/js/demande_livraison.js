
function validateForm(){
    var date = document.getElementById("date");
    var num_ramassage = document.getElementById("num_ramassage");
    var lieux_ramassage = document.getElementById("lieux_ramassage");
    var num_livraison = document.getElementById("num_livraison");
    var commune_liv = document.getElementById("commune_liv");
    var montant = document.getElementById("montant");
    var contact_depot = document.getElementById("contact_depot");
   
    var enregistrer = document.getElementById("enregistrer"); 

    if (date === "") {
        return false;
      }      

    if (num_ramassage === " "){
        alert("Vous devez entrer un num_ramassage");
        return false;
    }
    if (lieux_ramassage === " "){
        alert("Vous devez entrer un lieux");
        return false;  
    }
    if (num_livraison === " "){
        alert("Vous devez entrer un chiffre");
        return false;
    }
    else if (num_livraison < 18){
        alert("Entrez un contacte valide");
        return false;
    }
    if (commune_liv == " "){
        alert("Vous devez entrer le genre de l'employé");
        return false;
    }
    if (montant == " "){
        alert("Vous devez entrer le genre de l'employé");
        return false;
    }
    if (contact_depot == " "){
        alert("Vous devez entrer le genre de l'employé");
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
        html += "<td>" + element.date+ "</td>";
        html += "<td>" + element.num_ramassage + "</td>";
        html += "<td>" + element.lieux_ramassage + "</td>";
        html += "<td>" + element.num_livraison+ "</td>";
        html += "<td>" + element.commune_liv + "</td>";
        html += "<td>" + element.montant + "</td>";
        html += "<td>" + element.contact_depot+ "</td>";
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
        var date = document.getElementById("date").value;
        var num_ramassage = document.getElementById("num_ramassage").value;
        var lieux_ramassage = document.getElementById("lieux_ramassage").value;
        var num_livraison = document.getElementById("num_livraison").value;
        var commune_liv = document.getElementById("commune_liv").value;
        var montant = document.getElementById("montant").value;
        var contact_depot = document.getElementById("contact_depot").value;
       

        var peopleList;
        if (localStorage.getItem("peopleList") == null){
            peopleList = [];
        } else {
            peopleList = JSON.parse(localStorage.getItem
            ("peopleList"));
        }
        peopleList.push({
            date: date,
            num_ramassage : num_ramassage,
            lieux_ramassage : lieux_ramassage,
            num_livraison : num_livraison,
            commune_liv : commune_liv, 
            montant : montant,
            contact_depot : contact_depot,
        });
        localStorage.setItem("peopleList", JSON.stringify
        (peopleList));
        showData();
        document.getElementById("date").value = "";
        document.getElementById("num_ramassage").value = "";
        document.getElementById("lieux_ramassage").value = "";
        document.getElementById("num_livraison").value = "";
        document.getElementById("commune_liv").value = "";
        document.getElementById("montant").value = "";
        document.getElementById("contact_depot").value = "";
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