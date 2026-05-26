# 1) ახსენით რას აკეთებს lower მეთოდი და მოიყვანეთ მაგალითი
# lower- მეთოდი ყველა ასოს გადააქცევს პატარა ასოდ/lower case-ად,
"GOGA".lower()
# GOGA ---> goga


# 2) შექმენით სტრინგი დიდი ასოებით. lower მეთოდის გამოყენებით გადააკეთეთ ყველა ასო პატარად და დაპრინტეთ შედეგი
word = "WORLD"
word = word.lower()
print(word)

# 3) ახსენით რას აკეთებს upper მეთოდი და მოიყვანეთ მაგალითი
# upper - ყველა სიმბოლოს აქცევს დიდ ასოდ/upper case-ად
word = "example"
print(word.upper())

# 4) მომხმარებელს შემოატანინეთ სიტყვა. upper მეთოდის გამოყენებით გადააკეთეთ ეს სიტყვა დიდ ასოებად
word = input("enter a word: ")
word = word.upper()
print(word)


# 5) ახსენით რას აკეთებს title მეთოდი და მოიყვანეთ მაგალითი
# title - მეთოდი ადიდებს პირველ ასოს ყველა სიტყვაში
word = "hello world".title()
print(word)

# 6) შექმენით სტრინგების სია. გამოიყენეთ title მეთოდი თითოეულ სტრინგზე
strings = ["goga", "hello", "coding", "chess"]
for i in range(len(strings)):
    strings[i] = strings[i].title()
print(strings)
# 7) შექმენით სტრინგი, სადაც შერეული იქნება დიდი და პატარა ასოები. swapcase მეთოდის გამოყენებით შეცვალეთ ასოების ზომები და დაპრინტეთ შედეგი
word = "My NAme IS GogA"
word = word.swapcase()
print(word)

# 8) შექმენით სტრინგი. count მეთოდის გამოყენებით დაითვალეთ რამდენჯერ გვხვდება კონკრეტული ასო
word = "hello world"
print(word.count("l"))


# 9) მომხმარებელს შემოატანინეთ წინადადება და ერთი სიმბოლო. count მეთოდის გამოყენებით გაიგეთ რამდენჯერ გვხვდება ეს სიმბოლო წინადადებაში
sentence = input("enter random words: ")
symbol = input("enter a symbol ")
print(sentence.count(symbol))

# 10) მომხმარებელს შემოატანინეთ სახელი და გვარი. title მეთოდის გამოყენებით სწორ ფორმატში დაპრინტეთ ორივე.
name = input("Enter your name: ")
surname = input("Enter your surname: ")
print(name.title())
print(surname.title())

# 11) მომხმარებელს შემოატანინეთ წინადადება(დიდი ასოებითაც და პატარებითაც). დათვალეთ ხმოვნების რაოდენობა.

text = input("Enter a sentence: ")
text = text.lower()
vowels = "aeiou"
count = 0
for i in range(len(text)):
    if text[i] in vowels:
        count = count + 1

print(count)



# 12) მომხმარებელს შემოატანინეთ წინადადება(დიდი ასოებითაც და პატარებითაც).
#   - გაიგეთ დიდი ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ პატარა ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ ხმოვანი ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ თანხმოვანი ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ სფეისების პროცენტული რაოდენობა სტრინგში
sentence = input("enter random words: ")
lower_letters = "qazwsxedcrfvtgbyhnujmikolp"
lowercase = 0
for i in range(len(sentence)):
    if sentence[i] in lower_letters:
        lowercase = lowercase + 1

# ver gavige




