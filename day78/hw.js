// 1) დაწერეთ ფუქნცია, სახელად sayHello, რომელიც დაპრინტავს - "Hello, World".
function hello() {
    console.log("Hello, World")
}

// 2) დაწერეთ ფუნქცია, სახელად greet, რომელიც პარამეტრა მიიღებს სახელს და დაპრინტავს - "გამარჯობა, [სახელი]"
function greet(name) {
    console.log("გამარჯობა, " + name)
}

// 3) დაწერეთ ფუნქცია, სახელად sum, რომელიც არგუმენტებად მიიღებს ორ რიცხვს და დააბრუნებს მათ ჯამს. შედეგი გამოიტანეთ ტერმინალში.
function sum(num1, num2) {
    return num1 + num2
}
console.log(sum(5, 10))

// 4) დაწერეთ ფუნქცია, სახელად calculateArea, რომელიც არგუმენტად მიიღებს ოთხკუთხედის სიგრესა და სიგანეს და დააბრუნებს მის ფართობს. შედეგი გამოიტანეთ ტერმინალში.
function area(length, width) {
    return length * width
}
console.log(area(4, 5))

// 5) დაწერეთ ფუნქცია, რომელიც მიიღებს ორ არგუმენტს და დააბრუნებს მათ შორის უდიდესს.
function max(num1, num2) {
    if (num1 > num2) {
        return num1
    } else {
        return num2
    }
}

// 6) დაწერეთ ფუქნცია, რომელიც პარამეტრად მიიღებს იმ რაოდენობას, რამდენჯერად უნდა გამოკონსოლდეს "Hello, World".
function amount(console_amount){
    
}


// 7) დაწერეთ ფუქნცია, სახელად celsiusToFahrenheit, რომელიც პარამეტრად მიიღებს ცელსიუსს და გადაიყვანს ფარენჰეიტში. ფორმულა - (Celsius * 9/5) + 32
function celsiustofahrenheit(celsius) {
    return (celsius * 9/5) + 32
}