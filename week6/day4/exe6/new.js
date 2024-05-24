let names = ["alice", 42, "bob", null, "CHARLIE", undefined, "david", 0, "edward", "", "frank"];

// Get the output div elements
let modifiedNamesDiv = document.getElementById("modified-names");
let displayedNamesDiv = document.getElementById("displayed-names");

// First loop: Modify names if they are strings and their first letter is not uppercase
for (let i = 0; i < names.length; i++) {
    let item = names[i];
    
    if (typeof item !== "string") {
        continue;
    }
    
    if (item.charAt(0) !== item.charAt(0).toUpperCase()) {
        item = item.charAt(0).toUpperCase() + item.slice(1);
    }
    
    // Display the modified name
    let nameDiv = document.createElement("div");
    nameDiv.textContent = item;
    modifiedNamesDiv.appendChild(nameDiv);
}

for (let i = 0; i < names.length; i++) {
    let item = names[i];
    
    if (typeof item !== "string") {
        break; 
    }
    
    // Display the name
    let nameDiv = document.createElement("div");
    nameDiv.textContent = item;
    displayedNamesDiv.appendChild(nameDiv);
}
