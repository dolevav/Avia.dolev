console.log("Avia Dolev");
function thankyou() {
    document.getElementById("Button").innerHTML = "Thank you";
    console.log("thank you, Avia dolev");
}



function myFunction() {
    const inpObj = document.getElementById("Fid");
let idOK = inpobj.checkValidity();
if (idOK) {
    alert("id is OK");
}
else {
    alert("check your id");
}
}

/*function myFunction() {
    const inpObj = document.getElementById("Fid");
    if (!inpObj.checkValidity()) {
 document.getElementById("demo").innerHTML = inpObj.validationMessage;
    } else {
 document.getElementById("demo").innerHTML = "Input OK";
 }
 }
 */


