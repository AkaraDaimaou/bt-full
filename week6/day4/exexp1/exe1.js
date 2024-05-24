function runExercises() {
    // Exercise 1: List Of People
  
    const people = ["Greg", "Mary", "Devon", "James"];
  
    // Part I - Review About Arrays
  
    // Remove “Greg” from the people array
    people.shift();
    console.log(people); // ["Mary", "Devon", "James"]
  
    // Replace “James” with “Jason”
    people[people.indexOf("James")] = "Jason";
    console.log(people); // ["Mary", "Devon", "Jason"]
  
    // Add your name to the end of the people array
    people.push("Veer");
    console.log(people); // ["Mary", "Devon", "Jason", "YourName"]
  
    // Console.log Mary’s index
    console.log(people.indexOf("Mary")); // 0
  
    // Make a copy of the people array excluding “Mary” and your name
    const newPeople = people.slice(1, 3);
    console.log(newPeople); // ["Devon", "Jason"]
  
    // Code that gives the index of “Foo”
    console.log(people.indexOf("Foo")); // -1
  
    // Create a variable called last which is the last element of the array
    const last = people[people.length - 1];
    console.log(last); // "YourName"
  
    // Part II - Loops
  
    // Using a loop to iterate through the people array and console.log each person
    for (let person of people) {
      console.log(person);
    }
  
    // Using a loop to iterate through the people array and exit the loop after console.logging “Devon”
    for (let person of people) {
      console.log(person);
      if (person === "Devon") {
        break;
      }
    }
  
    // Exercise 2: Your Favorite Colors
  
    const colors = ["blue", "red", "green", "yellow", "purple"];
    for (let i = 0; i < colors.length; i++) {
      console.log(`My #${i + 1} choice is ${colors[i]}`);
    }
  
    // Bonus: Use suffixes for the output
    const suffixes = ["st", "nd", "rd", "th", "th"];
    for (let i = 0; i < colors.length; i++) {
      console.log(`My ${i + 1}${suffixes[i]} choice is ${colors[i]}`);
    }
  
    // Exercise 3: Repeat The Question
  
    let number;
    do {
      number = prompt("Enter a number:");
    } while (number < 10);
  
    // Exercise 4: Building Management
  
    const building = {
      numberOfFloors: 4,
      numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
      },
      nameOfTenants: ["Sarah", "Dan", "David"],
      numberOfRoomsAndRent: {
        sarah: [3, 990],
        dan: [4, 1000],
        david: [1, 500],
      },
    };
  
    console.log(building.numberOfFloors); // 4
    console.log(building.numberOfAptByFloor.firstFloor); // 3
    console.log(building.numberOfAptByFloor.thirdFloor); // 9
  
    const secondTenant = building.nameOfTenants[1];
    console.log(secondTenant); // "Dan"
    console.log(building.numberOfRoomsAndRent[secondTenant.toLowerCase()][0]); // 4
  
    const sarahRent = building.numberOfRoomsAndRent.sarah[1];
    const davidRent = building.numberOfRoomsAndRent.david[1];
    const danRent = building.numberOfRoomsAndRent.dan[1];
    if (sarahRent + davidRent > danRent) {
      building.numberOfRoomsAndRent.dan[1] = 1200;
    }
    console.log(building.numberOfRoomsAndRent.dan[1]); // 1200 if condition is true, otherwise 1000
  
    // Exercise 5: Family
  
    const family = {
      father: "John",
      mother: "Jane",
      sister: "Emily",
      brother: "Jack"
    };
  
    for (let key in family) {
      console.log(key);
    }
  
    for (let key in family) {
      console.log(family[key]);
    }
  
    // Exercise 6: Rudolf
  
    const details = {
      my: 'name',
      is: 'Rudolf',
      the: 'raindeer'
    };
  
    let sentence = "";
    for (let key in details) {
      sentence += `${key} ${details[key]} `;
    }
    console.log(sentence.trim()); // "my name is Rudolf the raindeer"
  
    // Exercise 7: Secret Group
  
    const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
    const societyName = names.map(name => name[0]).sort().join('');
    console.log(societyName); 
  }
  