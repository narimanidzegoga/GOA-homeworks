# 1) ახსენით რას აკეთებს append მეთოდი და მოიყვანეთ მაგალითი
# append - ამატებს ელემენტს სიის ბოლოში მაგალითი:
my_list = [10,15,20,25]
my_list.append("goga")
print(my_list)
# 2) შექმენით ცარიელი სია. append მეთოდის გამოყენებით დაამატეთ მასში 5 სხვადასხვა რიცხვი და დაპრინტეთ სია
my_list = []
my_list.append(5)
my_list.append(7)
my_list.append(15)
my_list.append(18)
my_list.append(20)
print(my_list)

# 3) შექმენით სია სიტყვებით. remove მეთოდის გამოყენებით წაშალეთ ერთ-ერთი სიტყვა და დაპრინტეთ შედეგი
my_list = ["goga","nika","hello","chess"]
my_list.remove("hello")
print(my_list)

# 4) ახსენით განსხვავება remove და pop მეთოდებს შორის
# remove - შლის ელემენტს მთლიანად, pop- ამოაგდებს ელემენტს რომელიც შეგიძლია სხვაგან ან იმავე სიაში ჩაამატო

# 5) შექმენით სია რიცხვებით. pop მეთოდის გამოყენებით ამოიღეთ ბოლო ელემენტი და დაპრინტეთ როგორც ამოღებული ელემენტი, ასევე განახლებული სია
numbers = [1,3,6,7,9,10,14,15]
num = numbers.pop(6)
print(num)
print(numbers)
# 6) შექმენით სია. insert მეთოდის გამოყენებით ჩასვით ახალი ელემენტი სიის შუაში
numbers = [2,3,5,6,7,9,10]
numbers.insert(3,16)
print(numbers)

# 7) შექმენით რიცხვების სია. sort მეთოდის გამოყენებით დაალაგეთ ეს სია და დაბეჭდეთ შედეგი
numbers = [6,3,7,10,14,3,15]
numbers.sort()
print(numbers)

# 8) ახსენით როგორ მუშაობს reverse მეთოდი და მოიყვანეთ მაგალითი
# reverse - აბრუნებს სიას უკუღმა
example = [1,2,3,5,10]
example.reverse()
print(example)

# 9) შექმენით სია სიტყვებით. reverse მეთოდის გამოყენებით შეცვალეთ ელემენტების რიგი
words = ["goga", "hello", "nika", "world"]
words.reverse()
print(words)

# 10) შექმენით სია და გამოიყენეთ clear მეთოდი. რა შედეგი მიიღეთ?
random_list = [15, "hello" , "goga",True , "world" ,False]
random_list.clear()
print(random_list)
# სიიდან ყველა ელემენტი წაიშალა

# 11) შექმენით სია რიცხვებით. გამოიყენეთ index მეთოდი, რომ იპოვოთ კონკრეტული რიცხვის ინდექსი
numbers = [3,5,7,9,18,20]
print(numbers.index(9))

# 12) შექმენით სია სიტყვებით. მომხმარებელს მოთხოვეთ რაიმე სიტყვა.
#   - თუ ეს სიტყვა არის სიაში იპოვეთ რომელ ინდექსზე დგას ეს სიტყვა
#   - სხვა შემთხვევაში დაპრინტეთ 'ვერ მოიძებნდა'

words = ["name" ,"hello","chess","welcome","sport"]
word = input("enter a word: ")

if word in words:
    print(words.index(word))
else:
    print("ვერ მოიძებნა")


# 13) შექმენით ცარიელი სია. მომხმარებელს მოთხოვეთ 10 რიცხვი და დაამატეთ ისინი ამ სიაში.
numbers = []
for i in range(10):
    number = int(input("enter a number "))
    numbers.append(number)
print(numbers)


# 14) შექმენით ცარიელი სია. მომხმარებელს მოთხოვეთ 7 რიცხვი და დაამატეთ ისინი ამ სიაში. დაპრინტეთ ამ რიცხვებიდან უდიდესი და უმცირესი რიცხვები
numbers = []
for i in range(7):
    number = int(input("enter a number: "))
    numbers.append(number)
numbers.sort()
print("biggest: " + str(numbers[-1]))
numbers.reverse()
print("smallest: " + str(numbers[-1]))


# 15) (|HARD|) შექმენით ცარიელი სია. მომხმარებელს სათითაოდ მოთხოვეთ 10 რიცხვი. სიაში დაამატეთ რიცხვი თუ: 
#   - დადებითია და არის ლუწი
#   - უარყოფითია და არის კენტი
# საბოლოოდ გაიგეთ ამ რიცხვების საშუალო

numbers = []

for i in range(10):
    number = int(input("enter a number: "))
    if number > 0 and number % 2 == 0:
        numbers.append(number)
    elif number < 0 and number % 2 != 0:
        numbers.append(number)

total = 0
for i in range(len(numbers)):
    total = total + numbers[i]
average = total / len(numbers)

print(average)


