// Create the variables and give them values
let addressNumber = 5;
let addressStreet = "BenYehuda";
let country = "Israel";

// Create a globalAddress variable and use the variables to create a sentence
let globalAddress = `I live in ${addressStreet} ${addressNumber}, in ${country}`;

// Display the globalAddress in the HTML
document.getElementById("address").innerText = globalAddress;
