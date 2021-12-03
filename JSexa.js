var txt = "jfdfjklfdkf"; /*string*/
var txt1 = txt.length;
var txt2 = txt.slice(0,4); /*return 0-3*/
console.log(txt2);
var txt3 = 'Come visit microsoft!';
var txt4 = txt3.replace("microsoft", "BGU");
console.log(txt4);


const d = new Date();
console.log(d);
var h = d.getHours();
console.log(h);


if (h<12) {
    greetings = "good morning";
 } else if (h<17) {
     greetings = "good afternoon";
 }
 else{
     greetings = "good evening";
 };
 console.log(greetings);

 function greet() {
    document.getElementById("P").innerHTML=greetings;

 };

 var cars = ["toyota", "honda", "ford"];
 console.log(cars[0]);
 console.log(cars[1]);

 var i;
 for (i=0; i<cars.length;i++) {
     console.log(cars[i]);

 }

 


