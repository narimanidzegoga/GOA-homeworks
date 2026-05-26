# 1) შექმენით სტრინგი ზედმეტი სფეისებით დასაწყისში და ბოლოში. strip მეთოდის გამოყენებით მოაშორეთ ზედმეტი სფეისები
text = " hello world "
text = text.strip()

# 2) მომხმარებელს შემოატანინეთ სახელი ზედმეტი სფეისებით. მოაშორეთ ზედმეტი სფეისები და დაპრინტეთ შედეგი
name = input("enter a name with spaces")
print(name.strip())

# 3) მომხმარებელს შემოატანინეთ სიტყვა. შეამოწმეთ იწყება თუ არა "A" ასოთი startswith მეთოდის გამოყენებით
word = input("enter a random word: ")
print(word.startswith("A"))

# 4) მომხმარებელს შემოატანინეთ ვებსაიტის მისამართი. შეამოწმეთ იწყება თუ არა "https"-ით
website = input("enter a website address")
print(website.startswith("https"))


# 5) მომხმარებელს შემოატანინეთ ფაილის სახელი. შეამოწმეთ მთავრდება თუ არა .py-ზე endswith მეთოდის გამოყენებით
file = input("Enter file name: ")
print(file.endswith(".py"))



# 6) მომხმარებელს შემოატანინეთ ელფოსტა. შეამოწმეთ მთავრდება თუ არა "@gmail.com"-ზე
email = input("enter your email: ")
print(email.endswith("@gmail.com"))


# 7) შექმენით ტექსტი. `replace()` მეთოდის გამოყენებით შეცვალეთ სიტყვა "dog" სიტყვით "cat"
text = "dog"
text = text.replace("dog", "cat")
print(text)

# 8) მომხმარებელს შემოატანინეთ წინადადება. ყველა სფეისი შეცვალეთ "-" სიმბოლოთი
text = input("enter a sentence: ")
text = text.replace(" ", "-")
print(text)

# 9) მომხმარებელს შემოატანინეთ ტელეფონის ნომერი ფორმატით "599-12-34-56". replace მეთოდის გამოყენებით წაშალეთ ყველა "-" სიმბოლო
number = input("Enter phone number: ")
number = number.replace("-", "")
print(number)



# 10) მომხმარებელს შემოატანინეთ ტექსტი ზედმეტი სფეისებით. ჯერ strip მეთოდით მოაშორეთ ზედმეტი სფეისები,
#  შემდეგ შეამოწმეთ იწყება თუ არა ტექსტი "Hello" სიტყვით
text = input("Enter text: ")
text = text.strip()

print(text.startswith("Hello"))



# 11) მომხმარებელს შემოატანინეთ პაროლი. შეამოწმეთ:
# - იწყება თუ არა დიდი ასოთი
# - მთავრდება თუ არა ციფრით "1"
password = input("Enter password: ")
print(password[0] in "QAZWSXEDCRFVTGBYHNUJMIKOLP")

print(password.endswith("1"))

# 12) მომხმარებელს შემოატანინეთ წინადადება. პროგრამამ უნდა:
# - მოაშოროს ზედმეტი სფეისები
# - ყველა სფეისი შეცვალოს "_" სიმბოლოთი
# - შეამოწმოს მთავრდება თუ არა "." სიმბოლოზე
# - თუ არ მთავრდება, ბოლოში დაამატოს "."
text = input("Enter a sentence: ")
text = text.strip()
text = text.replace(" ", "_")
if text.endswith("."):
    print(text)
else:
    text = text + "."
    print(text)


# 13) მომხმარებელს შემოატანინეთ სრული სახელი (სახელი, გვარი, მამის სახელი). `split()` მეთოდის გამოყენებით:
# - ცალ-ცალკე გამოიტანეთ თითოეული ნაწილი
# - დაითვალეთ რამდენი სიტყვაა შეყვანილ ტექსტში

fullname = input("enter you name, lastname, and father's name: ")
fullname = fullname.split()
print(fullname[0])
print(fullname[1])
print(fullname[2])

print(len(fullname))


# 14) მომხმარებელს შემოატანინეთ წინადადება. პროგრამამ უნდა:
# - დაყოს ტექსტი სიტყვებად
# - გამოიტანოს ყველაზე გრძელი სიტყვა
# - გამოიტანოს ყველაზე მოკლე სიტყვა
sentence = input("enter a sentence: ")
words = sentence.split()
longest = words[0]
shortest = words[0]
for i in range(len(words)):
    if len(words[i]) > len(longest):
        longest = words[i]
    if len(words[i]) < len(shortest):
        shortest = words[i]
print(longest)
print(shortest)




# 15) მომხმარებელს შემოატანინეთ რამდენიმე რიცხვი ერთი სტრინგის სახით (მაგ: "10 25 7 90 13"). split მეთოდის გამოყენებით:
# - გადააქციეთ ისინი integer-ებად
# - იპოვეთ ჯამი
# - იპოვეთ ყველაზე დიდი და ყველაზე პატარა რიცხვი

numbers = input("enter numbers: ")
numbers = numbers.split()
total = 0
biggest = int(numbers[0])
smallest = int(numbers[0])

for i in range(len(numbers)):
    total += int(numbers[i])

    if int(numbers[i]) > biggest:
        biggest = int(numbers[i])
    if int(numbers[i]) < smallest:
        smallest = int(numbers[i])

print("Sum:", total)
print("Biggest:", biggest)
print("Smallest:", smallest)







