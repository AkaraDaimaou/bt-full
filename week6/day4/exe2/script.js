// Create the variables and give them values for address
let addressNumber = 5;
let addressStreet = "BenYehuda";
let country = "Israel";

let globalAddress = `I live in ${addressStreet} ${addressNumber}, in ${country}`;

document.getElementById("address").innerText = globalAddress;

let birthYear = 2003;
let futureYear = 2030; 

let age = futureYear - birthYear;

let ageMessage = `I will be ${age} in ${futureYear}`;

document.getElementById("age").innerText = ageMessage;
