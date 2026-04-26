# 1) ახსენით რა არის mutable და immutable?
# mutable - ნიშნავს ცვლადის შექმნის შემდეგ მისი შეცვლა შესაძლოა
# immutable - ნიშნავს რომ ერთხელ შექმნის შემდეგ მისი შეცვლა არ შეიძლება

# 2) ახსენით რას აკეთებს len ფუნქცია
# len- ითვლის ელემენტების რაოდენობას

# 3) შექმენით ცვლადი სადაც შეინახავთ რაიმე სიტყვას. დაპრინტეთ რამდენი სიმბოლოა ამ სიტყვაში

word = "money"
print(len(word))

# 4) შექმენით ცვლადი სადაც მომხმარებელს შემოაყვანინებთ რაიმე წინადადაებას. დაპრინტეთ სიმბოლოების რაოდენობა ამ წინადადებაში

sentence = input("enter random words: ")
print(len(sentence))


# 5) შექმენით სია სადაც შეინახავთ რიცხვებს. for loop ის გამოყენებით დაითვალეთ რამდენი დადებითი და რამდენი უარყოფითი რიცხვია ამ სიაში

positive = 0
negative = 0

numbers = [5,10,-8,15,-20]
for i in range(len(numbers)):
    if numbers[i] > 0:
        positive = positive + 1
    elif numbers[i] < 0:
        negative = negative + 1
print(positive)
print(negative)

# 6) შექმნეით სია სადაც შეინახავთ რიცხვებს. დაითვალეთ რამდენი რიცხვი არის ამ სიაში ისეთი, რომელიც იყოფა 5-ზე


nums = [2,5,9,10.5,15,23,20]
g = 0

for i in range(len(nums)):
    if nums[i] % 5 == 0:
        g = g + 1
print(g)

# 7) შექმენით სია სადაც შეინახავთ რიცხვებს. დაპრინტეთ მხოლოდ ისეთი რიცხვები, რომლებიც იყოფა 4-ზეც და 7-ზეც
numbers = [5,7,8,12,19,26,28,56,80]
count = 0
for i in range(len(numbers)):
    if numbers[i] % 7 == 0 and numbers[i] % 4 == 0:
        count = count + 1
print(count)


# 8) შექმენით სია სადაც შეინახავთ ნებისმიერ მნიშვნელობებს. დაპრინტეთ მხოლოდ ის ელემენტები, რომლებიც იმყოფებიან ლუწ ინდექსზე

random = ["one", "boom", "money", "coding", "python", "focus", "game"]
for i in range(len(random)):
    if i % 2 == 0:
        print(random[i])

# 9) შექმენით სია სადაც შეინახავთ სიტყვებს. დაითვალეთ იმ სიტყვების რაოდენობა, რომელთა სიგრძეც მეტია 5-ზე

words = ["apple", "banana", "computer", "cat", "elephant", "sky"]

count = 0
for i in range(len(words)):
    if len(words[i]) > 5:
        count = count + 1
print(count)


# 10) შექმენით ცვლადი, რომელშიც შეინახავთ რაიმე წინადადებას. for ლუპის გამოყენებით დაპრინტეთ თითოეული სიმბოლო
sentence = "i like coding"
for i in range(len(sentence)):
    print(sentence[i])

# 11) შექმენით ცვლადი, რომელშიც შეინახავთ რაიმე წინადადებას. for ლუპის გამოყენებით დაპრინტეთ თითოეული სიმბოლო გარდა გამოტოვებისა

sentence = "i like football maybe"
for i in range(len(sentence)):
    if sentence[i] != " ":
        print(sentence[i])

# 12) შექმენით სია სადაც შეინახავთ სიტყვებს. for ლუპის გამოყენებით დაპრინტეთ: 'სიტყვა - სიგრძე'

words = ["apple", "football", "sky", "banana", "python"]
for i in range(len(words)):
    print(words[i], len(words[i]))

