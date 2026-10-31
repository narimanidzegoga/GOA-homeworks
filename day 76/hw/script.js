const body = document.body

const title = document.createElement("h1")
title.innerText = "15 HTML Projects for Beginners"
body.appendChild(title)

const p1 = document.createElement("h2")
p1.innerText = "1. Personal Bio Page"
body.appendChild(p1)

const desc1 = document.createElement("p")
desc1.innerText = "Description: Create a simple webpage introducing yourself. Add a heading with your name, a paragraph about you, line breaks, and a horizontal line."
body.appendChild(desc1)

const tags1 = document.createElement("p")
tags1.innerText = "Tags Covered: <h1>, <p>, <br>, <hr>"
body.appendChild(tags1)

const res1 = document.createElement("p")
res1.innerText = "Result:"
body.appendChild(res1)

const nameH = document.createElement("h2")
nameH.innerText = "John Doe"
body.appendChild(nameH)

const bio = document.createElement("p")
bio.innerText = "Hello! My name is John Doe.\nI am learning web development and this is my very first HTML page."
body.appendChild(bio)

body.appendChild(document.createElement("hr"))

const bio2 = document.createElement("p")
bio2.innerText = "I love coding and exploring new technologies."
body.appendChild(bio2)

body.appendChild(document.createElement("hr"))

const p2 = document.createElement("h2")
p2.innerText = "2. Favorite Books/Movies List"
body.appendChild(p2)

const desc2 = document.createElement("p")
desc2.innerText = "Description: Make a page listing your favorite books (unordered list) and movies (ordered list)."
body.appendChild(desc2)

const tags2 = document.createElement("p")
tags2.innerText = "Tags Covered: <ul>, <ol>, <li>"
body.appendChild(tags2)

const res2 = document.createElement("p")
res2.innerText = "Result:"
body.appendChild(res2)

const bookH = document.createElement("h2")
bookH.innerText = "My Favorite Books"
body.appendChild(bookH)

const ul = document.createElement("ul")
const book1 = document.createElement("li")
book1.innerText = "Harry Potter"
ul.appendChild(book1)
const book2 = document.createElement("li")
book2.innerText = "The Hobbit"
ul.appendChild(book2)
const book3 = document.createElement("li")
book3.innerText = "Atomic Habits"
ul.appendChild(book3)
body.appendChild(ul)

const movieH = document.createElement("h2")
movieH.innerText = "My Favorite Movies"
body.appendChild(movieH)

const ol = document.createElement("ol")
const movie1 = document.createElement("li")
movie1.innerText = "Inception"
ol.appendChild(movie1)
const movie2 = document.createElement("li")
movie2.innerText = "Interstellar"
ol.appendChild(movie2)
const movie3 = document.createElement("li")
movie3.innerText = "Avengers: Endgame"
ol.appendChild(movie3)
body.appendChild(ol)

body.appendChild(document.createElement("hr"))