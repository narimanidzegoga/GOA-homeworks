// 1) ჯავასკრიპტის ფაილში შექმენი ორი ცვლადი რომელშიც შეინახავ რიცხვებს და შემდეგ შეკრიბე ისინი, შედეგი დააკონსოლე
// 2) შექმენი ცვლადი სადაც შეინახავ ორ სიტყვას, შემდეგ შეკრიბე ისინი და ნახე როგორი შედეგი გექნება
// 3) ახსენი რა არი DOM
// 4) დააკავშირე htmlის და ჯავასკრიპტის ფაილები ერთმანეთთან,
//  html ის ფაილში შექმენი h1, p და img თეგი რომელსაც წაიღებ ჯავასკრიპტის ფაილში და შეინახავ შესაბამის ცვლადებში,
//  საბოლოდ ცვლადში შენახული მნიშვნელობები დააკონსოლე

// 1)
let firstnumber = 16
let secondnumber = 26
let total = firstnumber + secondnumber
console.log(total)

// 2)
let word1 = "hello"
let word2 = "world"
let bothwords = word1 + word2

// 3)
// DOM - document object model - HTML-ის სტრუქტურა JavaScript-ისთვის

// 4)

const heading = document.getElementById('h1');
const paragraph = document.getElementById('p1');
const image = document.getElementById('img1');

console.log(heading)
console.log(paragraph)
console.log(image)

