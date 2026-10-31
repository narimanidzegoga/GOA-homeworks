# 1) ახსენით რას აკეთებს `return` ბრძანება ფუნქციაში და მოიყვანეთ მარტივი მაგალითი.
# return - აბრუნებს ფუნქციის შედეგს უკან
def example():
    return 26
print(example())

# 2) შექმენით ფუნქცია `greet()`, რომელიც აბრუნებს (return) ტექსტს: "Hello, World!".
# გამოიძახეთ ფუნქცია და დაპრინტეთ შედეგი.
def greet():
    return "hello, world!"

print(greet())


# 3) შექმენით ფუნქცია `square(number)`, რომელიც აბრუნებს რიცხვის კვადრატს.
# შეამოწმეთ რამდენიმე მნიშვნელობაზე.
def square(number):
    return number * number

print(square(2))
print(square(8))
print(square(15))


# 4) შექმენით ფუნქცია `add(a, b)`, რომელიც აბრუნებს ორი რიცხვის ჯამს.
# მომხმარებელს შემოატანინეთ ორი რიცხვი და გამოიყენეთ ფუნქცია.
def add(a, b):
    return a + b

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print(add(num1, num2))


# 5) შექმენით ფუნქცია `is_even(number)`, რომელიც აბრუნებს True თუ რიცხვი ლუწია და False თუ კენტია.
def is_even(number):
    return number % 2 == 0
print(is_even(4))
print(is_even(7))








