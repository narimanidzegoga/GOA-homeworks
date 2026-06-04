# 1) რა არის ფუნქცია? ახსენით საკუთარი სიტყვებით.
# ფუნქციით შეგვიძლია რაიმე კონკრეტული დავალება მარტივად შევასრულოთ

# 2) რატომ არის ფუნქციები საჭირო პროგრამირებაში? - ჩამოწერეთ მინიმუმ 3 მიზეზი
# ფუნქციები საჭიროა: კოდის მარტივად ხელახლა გამოყენებისთვის, კოდის წაკითხვის გასამარტივებლად და უფრო მოწესრიგებულია და სწრაფი

# 3) რა არის პარამეტრი (Parameter)?
# პარამეტრი არის ცვლადი რომელსაც ფუნქციის გასაკეთებლად ვიყენებთ

# 4) რა არის არგუმენტი (Argument)?
# რაიმე მნიშვნელობა რომელსაც ფუნქციას გადავცემთ გამოძახების დროს

# 5) რა განსხვავებაა პარამეტრსა და არგუმენტს შორის?
# პარამეტრი ცვლადია, არგუმენტი კი ამ ცვლადის მნიშვნელობა

# 6) შექმენით ფუნქცია repeat_word(word, count).
# - ფუნქციამ count-ჯერ უნდა დაბეჭდოს `word`
# - გამოიყენეთ for ციკლი
def repeat_word(word, count):
    for i in range(count):
        print(word)

# 7) შექმენით ფუნქცია print_numbers(start, end).
# - ფუნქციამ უნდა დაბეჭდოს ყველა რიცხვი start-დან end-მდე
def print_numbers(start, end):
    for i in range(start, end):
        print(i)

# 8) შექმენით ფუნქცია count_even(numbers).
# - პარამეტრად მიიღოს სია
# - დაითვალოს რამდენი ლუწი რიცხვია სიაში
# - გამოიტანოს შედეგი
count = 0
def count_even(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            count = count + 1
print(count)

# 9) შექმენით ფუნქცია count_vowels(text).
# - პარამეტრად მიიღოს სტრინგი
# - დაითვალოს რამდენი ხმოვანია ტექსტში
# - გამოიტანოს შედეგი
count = 0
vowels = "aeiou"
def count_vowels(text):
    for i in range(len(text)):
        if vowels in text[i]:
            count = count + 1
print(count)

# 10) შექმენით ფუნქცია longest_word(words).
# - პარამეტრად მიიღოს სიტყვების სია
# - გამოიტანოს ყველაზე გრძელი სიტყვა
longest = " "
def longest_word(words):
    for i in range(len(words)):
        if len(words[i]) > len(longest):
            longest = words[i]
print(longest)
# 11) შექმენით ფუნქცია filter_long_words(words, n).
# - პარამეტრად მიიღოს წინადადება
# - გამოიტანოს მხოლოდ ის სიტყვები, რომელთა სიგრძე n-ზე მეტია
def filter_long_words(words, n):
    for i in range(len(words)):
        if len(words[i]) > n:
print(words[i])


# 12) მომხმარებელს შემოატანინეთ რამდენიმე სახელი ერთი სტრინგის სახით (მაგ: "nika luka ana gio").
# - split მეთოდით გადააქციეთ სიად
# - შექმენით ფუნქცია name_lengths(names)
# - ფუნქციამ თითოეული სახელის გვერდით უნდა დაბეჭდოს მისი სიგრძე
def name_lengths(names):
    for i in range(len(names)):
        print(names[i], len(names[i]))
names1 = input()
names = names1.split()
name_lengths(names)



# 13) შექმენით ფუნქცია find_max(numbers).
# - პარამეტრად მიიღოს რიცხვების სია
# - ციკლის გამოყენებით იპოვოს ყველაზე დიდი რიცხვი
def find_biggest(numbers):
    biggest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > biggest:
            biggest = numbers[i]
print(biggest)


# 14) შექმენით ფუნქცია find_min(numbers).
# - პარამეტრად მიიღოს რიცხვების სია
# - ციკლის გამოყენებით იპოვოს ყველაზე პატარა რიცხვი
def find_min(numbers):
    smallest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
print(smallest)




# 15) შექმენით ფუნქცია remove_duplicates(numbers).
# - პარამეტრად მიიღოს სია
# - შექმნას ახალი სია დუბლიკატების გარეშე
# - გამოიტანოს შედეგი

# ver gavige





# 16) მომხმარებელს შემოატანინეთ რამდენიმე რიცხვი ერთი სტრინგის სახით (მაგ: "10 25 7 90 13").
# - split() მეთოდით დაყავით ელემენტებად
# - გადააქციეთ integer-ებად
# - შექმენით ფუნქცია `analyze_numbers(numbers)`
# - ფუნქციამ უნდა:
#   - გამოიტანოს ჯამი
#   - გამოიტანოს საშუალო არითმეტიკული
#   - გამოიტანოს ყველაზე დიდი რიცხვი
#   - გამოიტანოს ყველაზე პატარა რიცხვი
#   - დაითვალოს ლუწი რიცხვების რაოდენობა
numbers = input("enter a few numbers: ")
numbers = numbers.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

total = 0
average = 0
biggest = 0
smallest = 0
even_total = 0
def analyze_numbers(numbers):
    for i in range(len(numbers)):
        total = total + numbers[i]
    for i in range(len numbers):
        
# ver gavige 






