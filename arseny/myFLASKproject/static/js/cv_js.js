console.log("Avia Dolev");
function thankyou() {
    document.getElementById("Button").innerHTML = "Thank you";
    console.log("thank you, Avia dolev");
}


function validation() {
    let obj = document.getElementById("Email");
    let emailOK = obj.checkValidity();
    if (emailOK) {
        alert("good! email is OK");
    }
    else {
        alert("please check your email");
    }
}