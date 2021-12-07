var imgs = [ /*array*/
    "IMAGES/happy.jpg",
    "IMAGES/happy2.jpg"
];

var i=0;

function play() { /*rexorcia*/
    console.log("IN");
    setTimeout(() => { /*קיצור דרך להגדרת פונקציה*/
    document.getElementById("img").src= imgs[i];
    i++;
    if (i< imgs.length) {
        play()
    } else {
        i=0;
    }
    
}, 500); /*הפסקה בין ריצות בלולאה במיליסכונד*/

}

var person = { 
    Fname: "Alma",
    Lname: "Shchar",
    FullName: function(){ /*()=> קיצור להגדיר פונקציה*/
        var Full = this.Fname + "" + this.Lname;
        return Full;
    }

};
console.log(Person.FullName());

