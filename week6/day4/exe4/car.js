let age = prompt("Please enter your age:");

// Check the age and respond accordingly
if (age < 18) {
    alert("Sorry, you are too young to drive this car. Powering off.");
} else if (age == 18) {
    alert("Congratulations on your first year of driving. Enjoy the ride!");
} else if (age > 18) {
    alert("Powering On. Enjoy the ride!");
} else {
    alert("Invalid input. Please enter a numerical value.");
}
