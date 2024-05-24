let outputDiv = document.getElementById("output");

// Iterate from 0 to 15
for (let i = 0; i <= 15; i++) {
    // Check if the number is odd or even
    if (i % 2 === 0) {
        // Create a new div element for even numbers
        let evenDiv = document.createElement("div");
        evenDiv.textContent = `${i} is even`;
        outputDiv.appendChild(evenDiv);
    } else {
        // Create a new div element for odd numbers
        let oddDiv = document.createElement("div");
        oddDiv.textContent = `${i} is odd`;
        outputDiv.appendChild(oddDiv);
    }
}
