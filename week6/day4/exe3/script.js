// Create an object with properties "username" and "password"
let user = {
    username: "john_doe",
    password: "123456"
};

let database = [user];

// Create an array called "newsfeed" which contains 3 objects with properties "username" and "timeline"
let newsfeed = [
    {
        username: "alice",
        timeline: "Having a great day at the beach!"
    },
    {
        username: "bob",
        timeline: "Just finished reading an awesome book!"
    },
    {
        username: "charlie",
        timeline: "Learning JavaScript is so much fun!"
    }
];

let databaseDiv = document.getElementById("database");
database.forEach(user => {
    let userDiv = document.createElement("div");
    userDiv.innerHTML = `<strong>Username:</strong> ${user.username}<br><strong>Password:</strong> ${user.password}`;
    databaseDiv.appendChild(userDiv);
});

let newsfeedDiv = document.getElementById("newsfeed");
newsfeed.forEach(news => {
    let newsDiv = document.createElement("div");
    newsDiv.innerHTML = `<strong>Username:</strong> ${news.username}<br><strong>Timeline:</strong> ${news.timeline}`;
    newsfeedDiv.appendChild(newsDiv);
});